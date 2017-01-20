var Yelp = require('yelpv3');

var yelp = new Yelp({
});

yelp.search({term: 'food', location: '08618', limit: 10})
.then(function (data) {
    console.log(data);
})
.catch(function (err) {
    console.error(err);
});