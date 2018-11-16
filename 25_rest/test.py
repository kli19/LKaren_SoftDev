#Karen Li
#SoftDev1 pd07
#K24 -- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import urllib, json
from urllib.request import Request, urlopen
app = Flask(__name__) 

@app.route("/") 
def hello_world():
    print("-----------------\n")
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request("https://api.openbrewerydb.org/breweries/1", headers=hdr)
    url_object=urlopen(req)
    print(url_object)
    info = url_object.read()
    print("-----------------\n")
    print(info)
    dict = json.loads(info)
    print("-----------------\n")
    return render_template("test.html",
                           brewery_name=dict["name"],
                           brewery_street=dict["street"],
                           brewery_city=dict["city"],
                           brewery_state=dict["state"],
                           brewery_postal=dict["postal_code"],
                           brewery_country=dict["country"],
                           brewery_website=dict["website_url"]
    )
                           

if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
