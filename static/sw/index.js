
function sw_fail(reason)
{
   console.log("Installing the worker failed!:", reason);
return reason;
}

function sw_ready(registration)
{
    console.log("success!");
    if (registration.installing) {
	registration.installing.postMessage("Howdy from your installing page.");
    }
    else if (registration.active) {
	registration.active.postMessage("Howdy from your active page.");
    }

//return navigator.serviceWorker.ready
return registration;
}

function after_subscription(subscription) { // after subscription workes
  console.log('Subscribed');
  if (subscription.endpoint){
      console.log(subscription.endpoint);
  }
}

function subscription_error(err) {  
           console.warn('Error during getSubscription()', err);  
	 }


function handle_subscription(subscription) {  
  if (!subscription) {  
    return;  
  }
  reg.pushManager.subscribe({ userVisibleOnly: true });
}

function handle_ready(reg)
{  
  reg.pushManager.getSubscription()  
  .then(handle_subscription)
  .then(after_subscription)
  .catch(subscription_error);  
}


var serviceWorkerPath = "/sw.js";
navigator.serviceWorker.register(serviceWorkerPath).then(sw_ready, sw_fail);

// from https://developers.google.com/web/updates/2015/03/push-notifications-on-the-open-web
navigator.serviceWorker.ready.then(handle_ready);