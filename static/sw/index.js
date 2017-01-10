var overpass_module = require("../compare/overpass_client.js");
var compare_module = require("../compare/compare.js");

function sw_fail(reason)
{
   console.log("Installing the worker failed!:", reason);
  return reason;
}

function sw_ready(registration)
{
  console.log("success!");
  if (registration.installing) {
    console.log("ready installing");
    registration.installing.postMessage("Howdy from your installing page.");
  }
  else if (registration.active) {
    console.log("ready active");
    registration.active.postMessage("Howdy from your active page.");
  }

  overpass_module.registration=registration;
  overpass_module.on_check();

  //return navigator.serviceWorker.ready
  return registration;
}

function after_subscription(subscription) { // after subscription
  console.log('after subscription');

  if (subscription) {
    if (subscription.endpoint){
      console.log(subscription.endpoint);

      // set on part of the equasion
      overpass_module.endpoint=subscription.endpoint;

      // now check if both are there
      overpass_module.on_check();
    }
  }
  else{
    console.log('No subscription');
  }
}

function subscription_error(err) {  
  console.warn('Error during getSubscription()', err);  
}


function handle_subscription(subscription) {  

  // now check if both are there
  overpass_module.on_check();

  if (!subscription) {  
    return;  
  }
  reg.pushManager.subscribe({ userVisibleOnly: true });
}

function handle_ready(reg)
{  
  // save this one
  overpass_module.registration=reg;

  reg.pushManager.getSubscription()  
  .then(handle_subscription)
  .then(after_subscription)
  .catch(subscription_error);  
}

var serviceWorkerPath = "/sw.js";
overpass_module.on_init();

navigator.serviceWorker.register(serviceWorkerPath).then(sw_ready, sw_fail);

// from https://developers.google.com/web/updates/2015/03/push-notifications-on-the-open-web
navigator.serviceWorker.ready.then(handle_ready);