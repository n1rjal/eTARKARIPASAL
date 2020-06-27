from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Items,Transaction
from .forms import QuantityForm,ComplainForm
from django.contrib import sessions
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from hashlib import sha256
import datetime
import csv
# Create your views here.

def home(request):
    name  = request.GET.get("name")

    items = Items.objects.all()
    request.session["name"]=name
    
    print(request.session.get("name"))
    return render(request,"items/index.html",{"foods":items})

def cart(request):
    if request.method=="GET":
        ids=request.session.get("cart_items")
        items=[]
        
        if ids is not None:
            for id in ids:
                items.append(Items.objects.get(pk=id))
        
        #this has been changed to GET
        postdata=request.GET.getlist('quantity')
        wsum=0
        rsum=0
        #mathematics beshind the calculation
        wstatements=[]
        rstatements=[]

        current_trans={}
        current_trans[0]={
            "id":"id",
            "name":"Name",
            "wprice":"Wholesale Price",
            "rprice":"Retail Price",
            "quantity":"Quantity",
            "wsum":"Wholesale Sum",
            "rsum":"Retail Sum",
            "wcalc":"Wholesale Calculation",
            "rcalc":"Retail Calculation"
        }
        i=0
        for i,item in enumerate(postdata):
            

            #dict for current item
            curritem={}
            curritem['id']=items[i].id
            curritem['name']=items[i].name
            curritem['wprice']="Rs "+str(items[i].wprice)
            curritem['rprice']="Rs "+str(items[i].rprice)
            curritem['quantity']=str(item)+str(items[i].unit)
            #initial wholesale sum
            iniwsum=int(items[i].wprice) * int(item)
            curritem['wsum']="Rs "+str(iniwsum)

            #initial retailsum
            inirsum=int(items[i].rprice) * int(item)
            curritem['rsum']="Rs "+str(inirsum)

            wstatement="Rs "+str(items[i].wprice) +" x "+ item+" = Rs "+ str(iniwsum)
            curritem['wcalc']=wstatement

            wstatements.append(wstatement)
            
            rstatement="Rs "+str(items[i].rprice) +" x "+ item+" = Rs "+ str(inirsum)
            curritem['rcalc']=rstatement

            rstatements.append(rstatement)

            wsum+=iniwsum
            rsum+=inirsum
            current_trans[i+1]=curritem

        
        
        wtotal=wsum
        rtotal=rsum
        current_trans['total_items']=i+1
        current_trans['rtotal']="Rs "+str(rtotal)
        current_trans['wtotal']="Rs "+str(wtotal)
        qform=QuantityForm(request.POST)
        

        request.session["current_transaction"]=current_trans
        #lets save the data in this calculation
        return render(request,"items/cart.html",{"items":items,"wstatements":wstatements,
        "rstatements":rstatements,"qform":qform,
        'wtotal':wtotal,'rtotal':rtotal})


#@login_required        
def getcurrtransaction(request):
    currtrans=request.session['current_transaction']
    return JsonResponse(currtrans,safe=False)

@login_required
def addtocart(request,id):
    try:
        cartitems=request.session['cart_items']
    except:
        request.session['cart_items']=[]
    
    cartitems=request.session['cart_items']
    
    if not id in cartitems:
        cartitems.append(id)

    request.session['cart_items']=cartitems
    return redirect('homepage')

def removefromcart(request,id):
    ids=request.session.get("cart_items")
    
    #try:
    
    index=ids.index(id)
    ids.pop(index)
    
    if len(ids)!=0:
        request.session["cart_items"]=ids
    else:
        request.session.pop('cart_items')
    
    return redirect('cart')

def bill(request):
    currtrans=request.session.get('current_transaction')
    if currtrans is not None:
        return render(request,"items/bill.html",{"items":currtrans})
    else:
        return redirect('homepage')

def sucess(request):
    if request.session.get('current_transaction') is not None:
        codetotransfer=(str(datetime.datetime.today())+request.user.username).encode()
        code=sha256(codetotransfer).hexdigest()
        context={
            "tcode":code[0:8]
        }
        text=request.session['current_transaction']
        current_transaction=Transaction(user=request.user,transactiontext=text)
        return render(request,"items/sucess.html",context)
    else:
        return redirect('homepage')

def export(request):
    
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']='attachment; filename="currentbill.csv"'
    
    towrite=request.session["current_transaction"]
    
    writer=csv.DictWriter(response,fieldnames=[
    "Name",
    "Wholesale Price",
    "Retail Price",
    "Wholesale Sum",
    "Retail Sum",
    "Wholesale Calculation",
    "Retail Calculation",
    "user"])
    writer.writeheader()
    maxloop=list(range(1,(int(towrite['total_items'])+1)))
    print(maxloop)
    for i in maxloop:
        currcursor=towrite[str(i)]
        print(i)
        print("\n\n")
        content={

            "Name":currcursor["name"],
            "Wholesale Price":currcursor["wprice"],
            "Retail Price":currcursor["rprice"],
            "Wholesale Sum":currcursor['wsum'],
            "Retail Sum":currcursor["rsum"],
            "Wholesale Calculation":currcursor["wcalc"],
            "Retail Calculation":currcursor["rcalc"],
            "user":(request.user.username)
        }
        writer.writerow(content)
        print(content)
        
    
    return response

@csrf_exempt
def search(request):
    if request.method=="GET":
        
        searchquery=request.GET.get('search-query')
        items=Items.objects.filter(name__contains=searchquery)
        users=User.objects.filter(username__contains=searchquery)
        print(items)
        print(users)
        return render(request,"items/searchresults.html",{"items":items,"users":users})
    
    if request.method=="GET":
        return redirect('homepage')

def about(request):
    if request.method=="GET":
        cform=ComplainForm()
        return render(request,"items/about.html",{"cform":cform})
    
    if request.method=="POST":
        cform=ComplainForm(request.POST)
        if cform.is_valid():
            CFORM=cform.save(commit=False)
            if request.user is not None:
                CFORM.user=request.user
            else:
                CFORM.user=""
            
            CFORM.save()

            return render(request,"items/about.html",{"cform":cform})
        else:
            return render(request,"items/about.html",{"cform":cform})

