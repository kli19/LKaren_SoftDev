from flask import Flask, render_template
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign function to route
def hello_world():
    print("about to print __name__...")
    print(__name__)
    return "No hablo queso"

if __name__ == "__main__":
    app.debug = True #turn off when going live
    app.run()
