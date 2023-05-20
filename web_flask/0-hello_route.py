#!/usr/bin/python3
"""A script that starts a flask web application
   listening on 0.0.0.0, port 5000
"""
from web_flask.__init__ import app
@app.route('/', strict_slashes=False)

def hello():
    return ("Hello HBNB!")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
