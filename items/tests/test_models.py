from django.test import TestCase
from ..models import Items

# Create your tests here.
class ItemModelTestCase(TestCase):
    def setUp(self) -> None:
        pass        

    def test_item_created_(self)->None:
        item_created = Items.objects.create(
            name= "Alu",
            unit= "Kg",
            rprice= 60,
            wprice= 40
        )
        self.assertEqual("Alu",item_created.name)
        self.assertEqual("Kg",item_created.unit)
        self.assertEqual(60,item_created.rprice)
        self.assertEqual(40,item_created.wprice)

    def test_item_retrieve_success(self)->None:
        self.assertEqual(Items.objects.filter().count(),4)
        
        