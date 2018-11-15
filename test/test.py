#Karen Li
#SoftDev1 pd07
#K24 -- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import urllib, json
app = Flask(__name__) 

@app.route("/") 
def hello_world():
    print("-----------------\n")
    url_object = urllib.request.urlopen("https://www.boredapi.com/api/activity")
    print(url_object)
    info = url_object.read()
    print("-----------------\n")
    print(info)
    dict = json.loads(info)
    print("-----------------\n")
    activity = dict["activity"]
    return render_template("nasa.html", suggestion=activity)

if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
