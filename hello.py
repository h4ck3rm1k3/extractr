import flask
import json
from flask import Flask, request, send_from_directory
from flask_reloaded import Reloaded
from flask_debugtoolbar import DebugToolbarExtension
from flask_bower import Bower
import pprint
#from flask_webpack import Webpack
#webpack = Webpack()

import yelp

app = Flask(__name__)

app.debug = True
   
params = {
    'BOWER_TRY_MINIFIED' : False,
    'SECRET_KEY' : 'flskjsdf994994304023.,m.,mvxclds',
    'DEBUG_TB_PANELS': (    'flask_reloaded.panels.ReloadedDebugPanel',),
    'DEBUG' : True,
#    'WEBPACK_MANIFEST_PATH': 'static/compare/compare-manifest.json',
#    'WEBPACK_ASSETS_URL'  : 'static/',
}

app.config.update(params)
    
#webpack.init_app(app)

DebugToolbarExtension(app)
reloaded = Reloaded(app)
Bower(app)     
@app.route('/')
def hello_world():
    return 'Hello, World!'

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


import pprint

@app.route('/tweets/')
def tweets():
    return render_template('tweets.html')

@app.route('/facebook/')
def fb():
    return render_template('fb.html')

@app.route('/sw/', defaults={'path': ''})
@app.route('/sw/<path:path>')
@app.route('/sw/')
def sw(path=None):
    return render_template('sw.html')

@app.route('/sw.js')
def swjs():
    #return "todo"
    return app.send_static_file('sw/service_worker.js')

@app.route('/favicon.ico')
def favico():
    return app.send_static_file('favicon.ico')


@app.route('/compare/')
def compare():
    return render_template('comparemaps.html')

import yelp
@app.route('/yelp/v3/oauth2/token' , methods=['POST'] )
#@crossdomain(origin='*')
def yelp_token():
    return yelp.obtain_bearer_token()

@app.route('/yelp/v3businesses/search', methods=['GET' ]) #?term=food&location=08618&limit=10
def yelp_biz_search():
    # GET /yelp/v3businesses/search?term=food&location=08618&limit=10 HTTP/1.1
    # authorization: Bearer JX_3SDC9tLlj4OtGqs3jewsPWF0xV4nfrqIDdgAjKp3uLeZxDK9CZpU4K-zR9RYEgwCv8on63odsSRaobgNvO0eVdVJWCZ4IYuiCepWVFdM8m80NEtDG0KADtrGAWHYx
    # Cookie: rg_cookie_session_id=229187570
    bearer = request.headers['Authorization']
    bearer = bearer.replace('Bearer ','')
    #pprint.pprint(request.headers)
    #EnvironHeaders([('Host', 'h4ck3rm1k3zone1.ddns.net:25000'), ('Connection', 'keep-alive'), ('Cookie', 'rg_cookie_session_id=229187570'), ('Pragma', 'no-cache'),
    #('Authorization', 'Bearer JX_3SDC9tLlj4OtGqs3jewsPWF0xV4nfrqIDdgAjKp3uLeZxDK9CZpU4K-zR9RYEgwCv8on63odsSRaobgNvO0eVdVJWCZ4IYuiCepWVFdM8m80NEtDG0KADtrGAWHYx'), ('Content-Type', ''), ('Accept', '*/*'), ('Content-Length', ''), ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'), ('Accept-Language', 'en-US,en;q=0.8'), ('Accept-Encoding', 'gzip, deflate, sdch'), ('Cache-Control', 'no-cache'), ('Referer', 'http://h4ck3rm1k3zone1.ddns.net:25000/yelp/')])

    #bearer_token
    term = request.args['term']
    location = request.args['location']
    res =  yelp.search(bearer, term, location)
    #pprint.pprint(res)
    #return pprint.pformat(res)
    return flask.jsonify(**res)

@app.route('/yelp/')
def yelp2():
    return render_template('yelp.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=25000, debug=True)
