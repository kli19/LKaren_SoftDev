# Karen Li
# SoftDev1 pd7
# 
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def home():  
    

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    name = request.args.get("username")
    methodUsed = request.method 
    return render_template('template.html', username = name, method = methodUsed, greeting = "Hello")

if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
