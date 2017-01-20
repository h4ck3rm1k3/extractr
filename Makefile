all : compile test
	echo starting

compile :
	#	webpack --config yelp-webpack.config.js
	browserify static/compare/yelp.js --outfile static/compare/yelp-bundle.js

test :
	#python hello.py
	FLASK_DEBUG=1 PYTHONPATH=/home/mdupont/experiments FLASK_APP=hello.py python3 -m flask run --reload --debugger  --host=0.0.0.0 --port=25000
