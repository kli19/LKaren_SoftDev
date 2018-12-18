#Karen Li
#SoftDev1 pd07
#K24 -- Getting More REST
#2018-11-15

from flask import Flask, render_template
import urllib, json
app = Flask(__name__) 

@app.route("/") 
def hello_world():
    
    url_object = urllib.request.urlopen("https://openlibrary.org/api/books?bibkeys=ISBN:0385472579,LCCN:62019420&format=json")
    print("-------------------------\n")
    print(url_object)
    print("-------------------------\n")
    info = url_object.read()
    print("-------------------------\n")
    print(info)
    print("-------------------------\n")
    dict = json.loads(info)

  
    return render_template("index.html")
if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
