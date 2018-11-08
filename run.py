import os
import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_heading="Welcome")
    
@app.route("/solar-info")
def solar_info():
    data = []
    with open("data/solar-bodies-info.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("solar-info.html", page_heading="Solar System Info", solar_bodies_data=data)

@app.route("/solar-quiz")
def solar_quiz():
    data = []
    with open("data/questions.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("solar-quiz.html", page_heading="Solar System Quiz", question_list=data)



"""@app.route("/question/<int:id>")
def get_question(id):
    data = []
    q = data
    with open("data/questions.json", "r") as json_data:
        data = json.load(json_data)
        
    return str(id)"""
    
    
@app.route("/question/<int:q>")
def get_question(q):
    data = []
    with open("data/questions.json", "r") as json_data:
        data = json.load(json_data)
    q = data[1]["question"]
    a = data[1]["choices"]
        
    return q + " " + a[0] + " " + a[1] + " " + a[2]
    


    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
