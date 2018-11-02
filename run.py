import os
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/solar-info")
def solar_info():
    return render_template("solar-info.html")
    
@app.route("/solar-quiz")
def solar_quiz():
    return render_template("solar-quiz.html")
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)