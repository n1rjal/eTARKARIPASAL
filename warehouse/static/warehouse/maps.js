/*
var locations = [
            ['<h1>Bhaktapur WareHouse</h1> <br> A warehouse situated in Bhatapur. <br> Currently warehouse holds more than 70 tons of vegetables <br><h4>Full Capacity : 100 tons</h4> <h4>Filled Capacity : 90 tons</h4> <h4>Free Capacity : 10 tons</h4>',27.672968,85.429291,'http://tarkariapp.herokuapp.com/?name=Kathmandu Warehouse '],
            ['<h1>Lalitpur WareHouse</h1> <br> A warehouse situated in Lalitpur. <br> Currently warehouse holds more than 30 tons of vegetables <br><h4>Full Capacity : 33 tons</h4> <h4>Filled Capacity : 32 tons</h4> <h4>Free Capacity : 1 tons</h4> ',24.687860,78.412018,'http://tarkariapp.herokuapp.com/?name=Lalitpur Warehouse'] ,
            ['<h1>Dolalghat WareHouse</h1> <br> A warehouse situated in Dolalghat. <br> Currently warehouse holds more than 90 tons of vegetables <br><h4>Full Capacity : 95 tons</h4> <h4>Filled Capacity : 80 tons</h4> <h4>Free Capacity : 15 tons</h4>',27.6329,85.7025,'http://tarkariapp.herokuapp.com/?name=Dolalghat Warehouse '],
            ['<h1>Barhabise WareHouse</h1> <br> A warehouse situated in Barhabise. <br> Currently warehouse holds more than 20 tons of vegetables <br><h4>Full Capacity : 25 tons</h4> <h4>Filled Capacity : 15 tons</h4> <h4>Free Capacity : 5 tons</h4>',27.8003, 85.9151,'http://tarkariapp.herokuapp.com/?name=Barhabise Warehouse '],
            ['<h1>Chautara WareHouse</h1> <br> A warehouse situated in Chautara. <br> Currently warehouse holds more than 45 tons of vegetables <br><h4>Full Capacity : 50 tons</h4> <h4>Filled Capacity : 45 tons</h4> <h4>Free Capacity : 5 tons</h4>',27.7761, 85.6948,'http://tarkariapp.herokuapp.com/?name=Chautara Warehouse ']
        ];
*/
function initMap(){
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
        center: new google.maps.LatLng(27.6329,85.7025),
    });

    var infowindow = new google.maps.InfoWindow();

    var marker, i;
    /*
    for (i = 0; i < locations.length; i++) {
            marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: map,
            url: locations[i][4]
        });
    */

        for (i = 0; i < whs.length; i++) {
            let locations=whs[i]
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations.lat, locations.lng),
                map: map,
                url: strurl
            })

            
        google.maps.event.addListener(marker, 'mouseover', (function(marker, i) {
            return function() {
                infowindow.setContent(locations.info);
                infowindow.open(map, marker);
            }
        })(marker, i));

        google.maps.event.addListener(marker, 'mouseout', (function(marker, i) {
            return function() {
                infowindow.close(map, marker);
            }        
        })(marker, i));


        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infowindow.setContent(locations.info);
                infowindow.open(map, marker);
                window.location.href = strurl;
            }
        })(marker, i));

    }
}