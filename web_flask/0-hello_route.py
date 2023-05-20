#!/usr/bin/python3
"""A script that starts a flask web application
   listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("AirBnB_clone_v2")
@app.route('/', strict_slashes=False)
def hello():
    return ("Hello HBNB!")
    if __name__ == "__main__":
         app.run(host="0.0.0.0", port=5000, debug=None)
