//
console.log('compare loaded');

function onload () {

  var storage=Storages.localStorage;
  var objs = {};

  if (!storage.isEmpty('osm_data')) {
    return;
  }

  // 
  
  var data = '';
  $.ajax({
    type: "GET",
    //url: 'http://overpass-api.de/api/interpreter?data=node%5B%22amenity%22%5D%2840%2E21912598956439%2C%2D74%2E87611770629881%2C40%2E318540592606354%2C%2D74%2E72522735595703%29%3Bout%20body%3B%0A',
    //url: 'http://localhost:5000/api/interpreter?data=node%5B%22amenity%22%5D%2840%2E21912598956439%2C%2D74%2E87611770629881%2C40%2E318540592606354%2C%2D74%2E72522735595703%29%3Bout%20body%3B%0A',
    url: '/bower/compare/ewing_amenities.xml',
    dataType: "xml",
    success: function (xml) {
      data = xml;

      data.childNodes[0].childNodes.forEach(
        function (n) {
          if (n.tagName == 'node') {
            var nid   = n.attributes['id'].nodeValue;
            var lat   = n.attributes['lat'].nodeValue;
            var lon   = n.attributes['lon'].nodeValue;
            var obj = {
              'nid' : nid,
              'lat' : lat,
              'lon' : lon
            };

            n.childNodes.forEach(
              function (t) {
                if (t.tagName == 'tag') {
                  var k   = t.attributes['k'].nodeValue;
                  var v   = t.attributes['v'].nodeValue;
                  obj[k]=v;
                }
              }
            );          
          }

          objs[nid]=obj;

        }// each node

      );

      // save
      storage.set('osm_data',objs);
    }// xml
  }
        );
  
}

function main () {
  // browserfy
  var foo = {
    data : function() {
      onload();
    }
  };
  foo.data();
}

main();
