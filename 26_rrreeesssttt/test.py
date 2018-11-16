#Karen Li
#SoftDev1 pd07
#K24 -- Getting More REST
#2018-11-15

from flask import Flask, render_template
import urllib, json
app = Flask(__name__) 

@app.route("/") 
def hello_world():
    
    url_object = urllib.request.urlopen("https://dog.ceo/api/breeds/image/random")
   # print("-------------------------\n")
   # print(url_object)
   # print("-------------------------\n")
    info = url_object.read()
   # print("-------------------------\n")
   # print(info)
   # print("-------------------------\n")
    dict = json.loads(info)
    image_url_2 = dict["message"]

    url_object = urllib.request.urlopen("https://catfact.ninja/fact")
   # print("-------------------------\n")
   # print(url_object)
   # print("-------------------------\n")
    info = url_object.read()
   # print("-------------------------\n")
   # print(info)
   # print("-------------------------\n")
    dict = json.loads(info)
    fact = dict["fact"]


    url_object = urllib.request.urlopen("https://aws.random.cat/meow")
   # print("-------------------------\n")
   # print(url_object)
   # print("-------------------------\n")
    info = url_object.read()
   # print("-------------------------\n")
   # print(info)
   # print("-------------------------\n")
    dict = json.loads(info)
    image_url_1 = dict["file"]

    return render_template("index.html", image1=image_url_1, image2=image_url_2, cat_fact=fact)

if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
