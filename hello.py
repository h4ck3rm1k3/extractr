import flask
import json
from flask import Flask, request, send_from_directory
from flask_reloaded import Reloaded
from flask_debugtoolbar import DebugToolbarExtension
from flask_bower import Bower
app = Flask(__name__)
app.debug = True
app.config['BOWER_TRY_MINIFIED']=False
app.config['SECRET_KEY'] = 'flskjsdf994994304023.,m.,mvxclds'
app.config['DEBUG_TB_PANELS'] = (
    # ...
    'flask_reloaded.panels.ReloadedDebugPanel',
)
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
    lt=type(hier)
    
    if lt==tuple:
        obj = hier
        name = obj[0]
        parent = obj[1]
        return {
            'name': str(name),
            'parent': str(parent),
        }
    elif lt==list:
        obj = hier[0]
        name = obj[0]
        parent = obj[1]
        alist = []
        for chl in hier[1:] :# children
            alist.append(traverse(chl))            
        return {
            'name': str(name),
            'parent': str(parent),
            'children': alist
        }

def cleantree():
    hier = inspect.getclasstree(onto.classes, unique=True)
    d = traverse(hier)
    return d
    
@app.route('/treedata/')
def get_tree():
    hier = cleantree()
    return "<html><body><h1>Hier</h1><pre>" + json.dumps(hier) +"</body></html>"

@app.route('/tree/')
def tree(name=None):
    hier = cleantree()
    return render_template('tree.html',hier=hier)

@app.route('/treed3/')
def treed3(name=None):
    hier = cleantree()
    return render_template('treed3.html',hier=hier)

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
