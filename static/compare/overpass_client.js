
var overpass_module = {
  'location' : null,
  'endpoint': null,
  'registration': null,

   'on_check' : function () {
     if (
       overpass_module.location
        &&
         overpass_module.registration
         //&&
       //overpass_module.endpoint
     ) {
       overpass_module.amenities(overpass_module.location);
     }
   },

  'on_init' :  function () {
    if ("geolocation" in navigator) {
      console.log("requesting position");
      navigator.geolocation.getCurrentPosition(function(position) {

        console.log("got position");
        overpass_module.location = position.coords;
        overpass_module.on_check();

      });
    } else {
      /* geolocation IS NOT available */
    }
  },
  'on_registered' : function () {
  },
    
  'base_url': 'http://overpass-api.de/api/interpreter?data=[out:json];',
    
  'query' : function (q) {
    console.log(q);
      $.ajax({
        type: "GET",
        //url: 'http://overpass-api.de/api/interpreter?data=' + encodeURIComponent(q),
        //url: '/overpass/query/' + encodeURIComponent(q),
        // 
        url: overpass_module.base_url + encodeURIComponent(q), 
        dataType: "json",
        success: function (json) {
          console.log(json);
        }
      })
    },
  'amenities' : function (location) {
    var height = 40.318540592606354 - 40.21912598956439;
    var width =  74.87611770629881  - 74.72522735595703;
    var lng = location.longitude;
    var lat = location.latitude;
    var coords = [
      lat  - (width /2) ,
      lng - (height/2) ,
      lat  + (width /2) ,
      lng + (height/2) ,
    ];   
    var query = 'node["amenity"](' +coords.join() +  ');out body;';
    overpass_module.query(query);
  }
    
};

// try and export this
exports = overpass_module;
module.exports = exports;