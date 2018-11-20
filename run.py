import os
import json
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "Some Secret"


"""Rendering the home page"""
@app.route("/")
def index():
    return render_template("index.html", page_heading="Welcome")
  
  
"""Rendering the solar info page"""   
@app.route("/solar-info")
def solar_info():
    data = []
    with open("data/solar-bodies-info.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("solar-info.html", page_heading="Solar System Info", solar_bodies_data=data)
        

"""Rendering the quiz"""
@app.route("/solar-quiz", methods=["GET", "POST"])
def solar_quiz():
    if request.method == "POST":
        write_to_file("data/names.txt", request.form["firstname"] + " " + request.form["lastname"] + "\n")
        flash("Thanks for playing {}. You scored {{ score }}/20. See where you rank on the leaderboard.".format(request.form["firstname"]))
        print(request.form)
    return render_template("solar-quiz.html", page_heading="Solar System Quiz")



"""The following functions take care of the printing of names and scores from the form to the text files and then printing to the leaderboard"""
def write_to_file(filename, data):
    """Handle the process of writing the data to the to files"""
    with open(filename, "a") as file:
        file.writelines(data)

def add_names():
    write_to_file("data/names.txt", request.form["firstname"] + " " + request.form["lastname"] + "\n")
    
def fetch_names_to_show():
    """Fetch all of the names from the text file"""
    show_names = []
    with open("data/names.txt", "r") as names:
        show_names = names.readlines()
    return show_names
    
    
    
"""Post quiz leaderboard rendering"""
@app.route("/solar-quiz/leaderboard")
def leaderboard():
    """Display the names from the text file"""
    show_names = fetch_names_to_show()
    return render_template("leaderboard.html", page_heading="Current Leaderboard", names=show_names)



"""Iterating through the questions from the solar-bodies-info.json file"""    
@app.route("/question/<int:id>") 
def get_question(id):
    data = []
    with open("data/questions.json", "r") as json_data:
        data = json.load(json_data)
    q = data[id - 1]["question"]
    c = data[id - 1]["choices"]
    return render_template("questions.html", question=data[id - 1])



"""Running the functions and rendering pages from above"""
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
