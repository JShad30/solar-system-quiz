import os
import json
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "username_collected"

score = 0


"""Calling the data from questions.json and putting it into a variable called questions"""
questions = []
with open("data/questions.json", "r") as json_data:
    questions = json.load(json_data)

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
    


"""Rendering the home page"""
@app.route("/")
def index():
    return render_template("index.html", page_heading="Welcome")
  
  
  
"""Rendering the solar info page"""   
@app.route("/solar_info")
def solar_info():
    data = []
    with open("data/solar-bodies-info.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("solar-info.html", page_heading="Solar System Info", solar_bodies_data=data)
        
        
        
"""Solar quiz and sub pages"""
"""Introducing the quiz and asking the player for their name to be presented later and written to the names file."""
@app.route("/solar_quiz", methods=["GET", "POST"])
def solar_quiz():
    if request.method == "POST":
        flash("Thanks for playing {0}. Your username is {1}, so be sure to look for it on the leaderboard at the end".format(request.form["firstname"], request.form["username"]))
        write_to_file("data/names.txt", request.form["firstname"] + " " + request.form["lastname"] + " - Username: " + request.form["username"] + "\n")
        return render_template("solar-quiz-user.html", page_heading="Solar System Quiz")
    return render_template("solar-quiz.html", page_heading="Solar System Quiz")



"""Iterating through the questions from the solar-bodies-info.json file"""    
@app.route("/solar_quiz/questions", methods=["GET", "POST"])#How to put the button in this part of the file to iterate through the questions?
def get_question():
    # Set score variable here? score = 0
    questions = []
    with open("data/questions.json", "r") as json_data:
        questions = json.load(json_data)
        """The following two lines were used when the questions were being displayed individually"""
        """q = questions[id - 1]["question"]
        c = questions[id - 1]["choices"]"""
        if request.method == "POST":
            flash("Thanks for playing {}. You scored {{ score }}/20. See where you rank on the leaderboard.")
            return render_template("quiz-completed.html", page_heading="Quiz Completed")
            
    return render_template("questions.html", page_heading="Quiz Questions", questions=questions)



"""Once last question is completed print the quiz"""
@app.route("/solar_quiz/quiz_completed", methods=["GET", "POST"])
def quiz_completed():
    return render_template("quiz-completed.html") 
    
   
    
"""Post quiz leaderboard rendering"""
@app.route("/solar_quiz/leaderboard")
def leaderboard():
    """Display the names from the text file"""
    show_names = fetch_names_to_show()
    return render_template("leaderboard.html", page_heading="Current Leaderboard", names=show_names)



"""Running the functions and rendering pages from above"""
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
