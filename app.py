# * Hello world flask app.

from flask import Flask

# ? Instantiate flask
# ? __name__ is going to be a different value depending on
# ? where you run flask from. If you run this directly,
# ? it will be '__main__'
app = Flask(__name__)

# ? Make a very basic route to talk to...
# * This @ syntax is a 'Decorator'. This decorator tell us
# * Which route our function belong to (our path for this route)
@app.route("/hello")
def home():
    return { "hello": "world" }
