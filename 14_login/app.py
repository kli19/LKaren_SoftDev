# Karen Li
# SoftDev1 pd7
# K #13: Echo Echo Echo .
# 2018-09-27

from flask import Flask, render_template, request, session, url_for, redirect
app = Flask(__name__) #create instance of class Flask
f = open("../key.py",'r')
app.secret_key = f.read()

user = "duck"
passwd = "goose"
@app.route("/")
def home():
    if (session["username"] == user and session["pass"] == passwd):
        return redirect(url_for("authenticate"))
    return render_template('form.html')
    

@app.route("/auth", methods=["POST", "GET"])
def authenticate():
    print(app)
    print(request)
    print(request.args)
	
    dictionary = {}

    if request.method=="GET":
        dictionary = request.args
		
    if request.method=="POST":
        dictionary = request.form

  

    if (dictionary["username"]==user):
        nameMessage = "CORRECT"
    else:
        nameMessage = "INCORRECT"

    if (dictionary["pass"]==passwd):
        passMessage = "CORRECT"
    else:
        passMessage = "INCORRECT"

    
    if(dictionary["username"] == user and dictionary["pass"]==passwd):
        session["username"] = user
        session["pass"] = passwd
    
    return render_template('results.html',
                        field0 = "username",
                        field1 = "password",
                        value0 = nameMessage,
                        value1 = passMessage,
                        header = "Welcome!",
                        message = "Thank you for your input.")

if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
