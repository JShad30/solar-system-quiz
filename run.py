import os
import json
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "username_collected"


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
    
    """Setting the inputed values as variables"""
    #username = form.request["username"] #Sets the username input as a variable
    #firstname = form.request["firstname"] #Sets the firstname input as a variable
    #lastname = form.request["lastname"] #Sets the lastname input as a variable
    
    if request.method == "POST":
        
        flash("Thanks for playing {0}. Your username is {1}, so be sure to look for it on the leaderboard at the end".format(request.form["firstname"], request.form["username"]))
        write_to_file("data/names.txt", request.form["firstname"] + " " + request.form["lastname"] + " - Username: " + request.form["username"] + "\n")
        return render_template("solar-quiz-user.html", page_heading="Solar System Quiz")
        
    return render_template("solar-quiz.html", page_heading="Solar System Quiz")



"""Iterating through the questions from the solar-bodies-info.json file"""    
@app.route("/solar_quiz/questions", methods=["GET", "POST"])#How to put the button in this part of the file to iterate through the questions?
def get_question():
    #Set the score variable to 0
    score = 0
    questions = []
    with open("data/questions.json", "r") as json_data:
        questions = json.load(json_data)
        if request.method == "POST":
            for question in questions: #This loop is supposed to iterate over the questions. Should this be done only in the questions.html though?"""
                correct_answer = question.answer() #Variable correct_answer looks for the 'answer' value in questions.json
                answer_given = request.form["choice-{{ question.id }}"] #Variable answer_given finds which was selected in questions.py
                """function to increase value of score by 1 if correct_answer is the same as answer_given"""
                def add_score(score):
                    if answer_given.lower() == correct_answer:
                        score += 1
                return score
            
            """At the end of the quiz when the score has been added display the correct message"""        
            if score == 20:
                flash("Thanks for playing {0}. You scored {1}/20. Well done, that is a perfect score! See yourself on the leaderboard.".format(request.form["username"], request.form[str(score)]))
            elif score >= 15:
                flash("Thanks for playing {0}. You scored {1}/20. That's a great score! See where you stand on the leaderboard.".format(request.form["username"], request.form[str(score)]))
            elif score >= 10:
                flash("Thanks for playing {0}. You scored {1}/20. That's a decent score! See where you stand on the leaderboard, or look at the info.".format(request.form["username"], request.form[str(score)]))
            else:
                flash("Thanks for playing {0}. You scored {1}/20. Have a look at the leaderboard, or the Solar Info page if you'd like to learn more about the solar system.".format(request.form["username"], request.form[str(score)]))
                
            """Displays the quiz-completed.html page with the flash message attached as above"""
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
