
from flask import Flask, request, send_from_directory


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

import owlready
from owlready import *
onto_path.append(os.path.dirname(__file__))
onto = Ontology("http://test.org/floss-events.owl")
onto.name = "floss-events"
onto.load()

@app.route('/onto/')
def info():
    return "Hello"

if __name__ == "__main__":
    app.run()
