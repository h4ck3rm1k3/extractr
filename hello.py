
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




if __name__ == "__main__":
    app.run()
