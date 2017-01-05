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

//
// this.addEventListener('install', function(event) {
//   console.log('install');
//   console.log(event);
// });

// // this.addEventListener('fetch', function(event) {
// //   console.log('fetch');
// //   console.log(event);
// // });

// this.addEventListener('ended', function(event) {
//   console.log('ended');
//   console.log(event);
// });

// this.addEventListener('loadeddata', function(event) {
//   console.log('loaded data');
//   console.log(event);
// });

// this.addEventListener('load', function(event) {
//   console.log('load');
//   console.log(event);
// });

// this.addEventListener('unload', function(event) {
//   console.log('unload');
//   console.log(event);
// });

// this.addEventListener('error', function(event) {
//   console.log('error');
//   console.log(event);
// });

// this.addEventListener('abort', function(event) {
//   console.log('abort');
//   console.log(event);
// });

// this.addEventListener('click', function(event) {
//   console.log('click');
//   console.log(event);
// });

// this.addEventListener('resize', function(event) {
//   console.log('resize');
//   console.log(event);
// });

// this.addEventListener('push', function(event) {
//   console.log('push');
//   console.log(event);
// });

// self.addEventListener('pushsubscriptionchange', function(event) {
//   console.log('push subscription change');
//   console.log(event);

// });

// this.addEventListener('active', function(event) {
//   console.log('active');
//   console.log(event);
// });

// this.addEventListener('notificationclick', function(event) {
//   console.log('notificationclick');
//   console.log(event);
// });

// this.addEventListener('notificationclose', function(event) {
//   console.log('notificationclose');
//   console.log(event);
// });

// this.addEventListener('message', function(event) {
//   console.log('message');
//   console.log(event);
//   //console.log(event.request.url);
// //event.respondWith(new Response("Hello world!"));
//   //IDBRequest
//   //IDBObjectStore
//   //IDBKeyRange
//   //IDBIndex
//   //IDBFactory
//   //IDBDatabase
//   //IDBCursor
// });

// this.addEventListener('hashchange', function(event) {
//   console.log('hashchange');
//   console.log(event);
// });

// this.addEventListener('complete', function(event) {
//   console.log('complete');
//   console.log(event);
// });

// this.addEventListener('success', function(event) {
//   console.log('success');
//   console.log(event);
// });

// this.addEventListener('statechange', function(event) {
//   console.log('statechange');
//   console.log(event);
// });

// this.addEventListener('fetch', function(event) {
//   console.log('fetch');
//   console.log(event);
// //  console.log(event.request.url);
//   console.log(".request", event.request);
//   console.log(".respondWith", event.respondWith);
//   console.log(".default", event.default);
//   if (event.request) {
//     console.log(event.request.url);
//   }
//   if (event.respondWith) {
//     event.respondWith(new Response(new Blob(["Hello <b>world</b>"], {type : 'text/html'}), {
//       headers: {"Content-Type": "text/html"}
//     }));
//   }
// });

self.toolbox.router.get(':foo/index.html', function(request, values) {
  return new Response('Handled a request for ' + request.url +
      ', where foo is "' + values.foo + '"');
});
self.toolbox.router.get('/funky/(.*)', function() {
  return new Response('/default');
});