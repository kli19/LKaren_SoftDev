# Karen Li
# SoftDev1 pd7
# K #13: Echo Echo Echo .
# 2018-09-27

from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class Flask

@app.route("/")
def home():
    return render_template('form.html')
    

@app.route("/auth", methods=["POST", "GET"])
def authenticate():
    print(app)
    print(request)
    print(request.args)
    name = request.args["username"]
    #name = request.form["username"]
    methodUsed = request.method 
    return render_template('results.html',
                           field0 = "username",
                           field1 = "method",
                           value0 = name,
                           value1 = methodUsed,
                           header = "This is the information we have received:",
                           message = "Thank you for your input.")

if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
