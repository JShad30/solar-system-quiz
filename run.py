import os
import json
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "Some Secret"



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
    
def next_question():
    """Moves the question page to the next question"""
    


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
        
        
        
"""Solar quiz and sub pages"""
"""Introducing the quiz and asking the player for their name to be presented later and written to the names file."""
@app.route("/solar-quiz", methods=["GET", "POST"])
def solar_quiz():
    if request.method == "POST":
        write_to_file("data/names.txt", request.form["firstname"] + " " + request.form["lastname"] + "\n")
    return render_template("solar-quiz.html", page_heading="Solar System Quiz")
    


"""Iterating through the questions from the solar-bodies-info.json file"""    
@app.route("/solar-quiz/question/<int:id>")#How to put the button in this part of the file to iterate through the questions?
def get_question(id):
    # Set score variable here? score = 0
    questions = []
    with open("data/questions.json", "r") as json_data:
        questions = json.load(json_data)
        # Loop here to iterate? for question in questions:
    q = questions[id - 1]["question"]
    c = questions[id - 1]["choices"]
    return render_template("questions.html", question=questions[id - 1])



"""Once last question is completed print the quiz"""
@app.route("/solar-quiz/quiz-completed", methods=["POST"])
def quiz_completed():
    if request.method == "POST":
        flash("Thanks for playing {}. You scored {{ score }}/20. See where you rank on the leaderboard.".format(request.form["firstname"]))
        print(request.form)
    return render_template("quiz-completed.html", page_heading="Solar System Quiz")
    
   
    
"""Post quiz leaderboard rendering"""
@app.route("/solar-quiz/leaderboard")
def leaderboard():
    """Display the names from the text file"""
    show_names = fetch_names_to_show()
    return render_template("leaderboard.html", page_heading="Current Leaderboard", names=show_names)



"""Running the functions and rendering pages from above"""
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
