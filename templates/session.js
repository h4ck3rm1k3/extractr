
// needs     <script type="text/javascript" src="../bower_components/js-storage/js.storage.js"></script>
//          <script type="text/javascript" src="../bower_components/jquery/dist/jquery.js"></script>

function get_session(){
  storage=Storages.localStorage;
  if (storage.isEmpty('session')) {
    $.get('http://h4ck3rm1k3.sdf.org/a/session/get',
	  function(data){
	    storage.set('session',data);
	  });
  }

  // return the session
  return storage.get('session');
}