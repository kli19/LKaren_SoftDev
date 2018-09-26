# OccupationalHazard: Karen Li, Ahnaf Hasan
# SoftDev1 pd07
# K #10: Jinja Tuning 
# 2018 - 09 - 24

from flask import Flask, render_template
from util import occupation
app = Flask(__name__)


@app.route("/")

def home():
    return "<a href='occupations'>Click to view the occupation table</a>"

@app.route("/occupations")

def template():

    return render_template('template.html', 
                            randOcc = occupation.randomOccupation(), 
                            occDict = occupation.occupationDic,
                            title = "Occupation Data",
                            header = "United States Occupations Information",
                            info = "This page shows occupations in the United States along with the percentage of the U.S. workforce it comprises."
                            ) 



if __name__ == "__main__":

    app.debug = True

    app.run()
