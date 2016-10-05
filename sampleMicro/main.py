from flask import Flask
app = Flask(__name__)
from ..muse import endpoint

@app.route("/")
def hello():
    return "Hello World!"


def getEndpoints():
    return []

if __name__ == "__main__":
    print "Starting up"
    app.run()
