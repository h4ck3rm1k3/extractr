//
function cb(data){
    console.log(data);
}

function overpass_query(request, query){
  //var xhr = new XMLHttpRequest();

  return {
    'todo': 1 ,
    'query': decodeURIComponent(query)
  }
}

exports = {
  'query' : overpass_query
}