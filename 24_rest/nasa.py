#Karen Li
#SoftDev1 pd07
#K24 -- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import urllib, json
app = Flask(__name__) 

@app.route("/") 
def hello_world():
     url_object = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?date=2015-01-01&api_key=vQel13DdBfcZ9IdHbivw0nuxaC6WtRuuPPqngd8H")
     #print(url_object)
     info = url_object.read()
     #print(info)
     dict = json.loads(info)
     #print(dict["url"])
     return render_template("nasa.html", image_url=dict["url"], explanation=dict["explanation"])

if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
