import flask
import json
from flask import Flask, request, send_from_directory
from flask_reloaded import Reloaded
from flask_debugtoolbar import DebugToolbarExtension
from flask_bower import Bower
#from flask_webpack import Webpack
#webpack = Webpack()

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
import owlready
from owlready import *
onto_path.append(os.path.dirname(__file__))
onto = load_ontology_from_file("floss-events.owl")
import types
import inspect

def traverse(hier):
    ret = []
    cobj = None
    for obj in hier :#
        lt=type(obj)
        if lt==tuple: # is an object
            name = obj[0]
            parent = obj[1]
            cobj= {
                'name': str(name),
                'parent': str(parent),
            }
            ret.append(cobj)            
        elif lt==list:
            cobj['children']=traverse(obj)
    if len(ret) == 1:
        return ret[0]
    else:
        return ret

def cleantree():
    hier = inspect.getclasstree(onto.classes, unique=True)
    d = traverse(hier)
    return d
    
@app.route('/treedata/')
def get_tree():
    hier2 = inspect.getclasstree(onto.classes, unique=True)
    hier = cleantree()
    return "<html><body><h1>Hier</h1><pre>" + json.dumps(hier) +"<pre><h1>Input</h1><pre>" + str(hier2) +"<pre></body></html>"

@app.route('/tree/')
def tree(name=None):
    hier = cleantree()
    return render_template('tree.html',hier=hier)

@app.route('/treed3/')
def treed3(name=None):
    hier = cleantree()
    return render_template('treed3.html',hier=hier)

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

#
#Property: EventWho,
#type:              Agent,
#                   Role

#Prop:     EventWhat,
# to what :
# PhysicalThing
# AbstractDocument
# via UserInterface
# DataResource
# to what that is formatted
# Dataformat
#type              Model,
# Event :

#Prop:     EventWhere
#            PhysicalLocation
#            DataResource

#Prop:     EventWhen,
#type:        Event,

# How
#Prop          EventWhy,
# cause, purpose : Model

#    Visitor declares interest in hearing a talk on topic X
#                 EventExpressesInterestInLearning,

 
@app.route('/onto/')
def info():
    b = onto.Bus()
    #pprint.pprint(b._instance_to_n3())
    #pprint.pprint(b._instance_to_owl())


    return "<html><body><h1>Hello</h1><pre>" + pprint.pformat(onto.__dict__) + "</pre><pre>"+ pprint.pformat(dir(onto)) + "</pre><pre>"+ pprint.pformat(b) + "</pre><pre>"+ pprint.pformat(dir(b)) + "</pre><pre>"+ pprint.pformat(b.__dict__)+"</body></html>"

if __name__ == "__main__":
    app.run(debug=True)
