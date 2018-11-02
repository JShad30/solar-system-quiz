import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", page_heading="Welcome")
    
@app.route("/solar-info")
def solar_info():
    data = []
    with open("data/solar-bodies-info.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("solar-info.html", page_heading="Solar System", solar_bodies_data=data)
    
@app.route("/solar-quiz")
def solar_quiz():
    return render_template("solar-quiz.html", page_heading="Solar Quiz")
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)