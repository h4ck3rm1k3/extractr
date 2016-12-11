
from flask import Flask, request, send_from_directory
from flask_reloaded import Reloaded
from flask_debugtoolbar import DebugToolbarExtension
from flask_bower import Bower
app = Flask(__name__)
app.debug = True
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

@app.route('/tree/')
def tree(name=None):
    return render_template('tree.html')

import pprint
import owlready
from owlready import *
onto_path.append(os.path.dirname(__file__))
onto = load_ontology_from_file("floss-events.owl")

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
