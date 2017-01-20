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
@app.route('/onto/')
def info():
    b = onto.Bus()
    #pprint.pprint(b._instance_to_n3())
    #pprint.pprint(b._instance_to_owl())


    return "<html><body><h1>Hello</h1><pre>" + pprint.pformat(onto.__dict__) + "</pre><pre>"+ pprint.pformat(dir(onto)) + "</pre><pre>"+ pprint.pformat(b) + "</pre><pre>"+ pprint.pformat(dir(b)) + "</pre><pre>"+ pprint.pformat(b.__dict__)+"</body></html>"
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

