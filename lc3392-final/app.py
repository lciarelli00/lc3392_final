# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

"""
Edited by Luke Ciarelli
lc3392
Flask server code, edits include routes.
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def 1006():
    return render_template("1006/index.html")
    
@app.route("/classes")
def classes():
    return render_template("classes/index.html")
    
@app.route("/music")
def music():
    return render_template("music/index.html")
    
#start the server
if __name__ == "__main__":
    app.run()