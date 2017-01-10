(global => {
  'use strict';

  var l4 = {
    importScripts: (function () {
                      var files = new Set();
                      return function() {
                        Array.prototype.forEach.call(arguments, function(fileName) {
                          if(!files.has(fileName)) {
                            files.add(fileName);
                            importScripts(fileName);
                          }
                        })
                      }
                    })()
  };


  //var pathToRegexp = l4.importScripts('path-to-regexp');
  l4.importScripts('bower/sw-toolbox/sw-toolbox-clean.js');  // Update path to match your own setup.
  l4.importScripts('static/sw/overpass.js');  // overpass api

  self.toolbox.options.debug = true;
  self.toolbox.router.get(':foo/index.html', function(request, values) {
    return new Response('Handled a request for ' + request.url +
                        ', where foo is "' + values.foo + '"');
  });
  self.toolbox.router.get('/funky/(.*)', function() {
    return new Response('/default');
  });

  self.toolbox.router.get('/overpass/query/:query', function(request, values) {
    return new Response('/overpass/query/' + JSON.stringify(overpass_query(request, values.query)));
  });

  self.toolbox.router.get('foo:/api/interpreter/:query', function(request, values) {
    return new Response('/overpass/query/' + JSON.stringify(overpass_query(request, values.query)));
  });

  // this.addEventListener('fetch', function(event) {
  //   console.log('fetch');
  //   console.log(event);
  // });

  toolbox.router.get(
    '(.*)',
    self.toolbox.cacheFirst,
    {      
      cache: {
        name: 'overpass',
        maxEntries: 10,
        maxAgeSeconds: 86400
      },
      origin: /overpass\-api\.de$/
    }
  );

  // just cache everything
   toolbox.router.get(
     '(.*)',
     self.toolbox.cacheFirst,
     {      
       cache: {
         name: 'all',
         maxEntries: 20,
         maxAgeSeconds: 86400
       },
     }
   );
  
  self.addEventListener('install', event => event.waitUntil(global.skipWaiting()));
  self.addEventListener('activate', event => event.waitUntil(global.clients.claim()));

})(self);