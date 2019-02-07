import os
import json
from flask import Flask, url_for, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "username_collected"


"""Calling the data from questions.json and putting it into a variable called questions"""
questions = []
with open("data/questions.json", "r") as json_data:
    questions = json.load(json_data)
    
    
"""Writing data received on forms to the json file"""
#with open("data/quizplayers.json", "w") as 
    

"""The following functions take care of the printing of names and scores from the form to the text files and then printing to the leaderboard"""
def write_to_file(filename, data):
    """Handle the process of writing the data to the to files"""
    with open(filename, "a") as file:
        file.writelines(data)

def add_names(firstname, lastname):
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
    if request.method == "POST":
        username = request.form["username"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        """Creating the sessions for the variables"""
        session['username'] = username
        session['firstname'] = firstname
        session['lastname'] = lastname
        """Setting the Variables"""
        flash("Thanks for playing {0}. Your username is {1}, so be sure to look for it on the leaderboard at the end".format(request.form["firstname"], request.form["username"]))
        write_to_file("data/names.txt", request.form["firstname"] + " " + request.form["lastname"] + " - Username: " + request.form["username"] + "\n")
        return render_template("solar-quiz-user.html", page_heading="Solar System Quiz", username=username, firstname=firstname, lastname=lastname)
        
    return render_template("solar-quiz.html", page_heading="Solar System Quiz")
    


"""Iterating through the questions from the solar-bodies-info.json file"""    
@app.route("/solar_quiz/<username>/question/<int:id>", methods=["GET", "POST"]) #How to put the button in this part of the file to iterate through the questions?
def get_question(username, id):
    #Set the score variable to 0
    questions = []
    print(request.form.items()) #Mentor suggestion to show in console below
    with open("data/questions.json", "r") as json_data:
        questions = json.load(json_data)
        q = questions[id - 1]["question"]
        c = questions[id - 1]["choices"]
        a = questions[id - 1]["answer"]
        for q in questions:
            if request.method == "POST":
                score = 0
                session['score'] = score
                id += 1
                if id > len(questions):
                    return redirect(url_for("quiz_completed", page_heading="Quiz Completed", username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score']))
                answer_given = request.form["choice"] #Variable answer_given finds which was selected in questions.py
                """function to increase value of score by 1 if correct_answer is the same as answer_given"""
                def add_score(): #create the function with score as an argument - currently set at 0
                    if answer_given == a: #Check whether answer given and correct answer are the same
                        score += 1 #if so add 1
                    return score #Return the final score when all answers added together
                return redirect(url_for("get_question", username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score'], id=id))
                
            return render_template("questions.html", page_heading="Quiz Questions", question=questions[id - 1], username=session['username'], firstname=session['firstname'], lastname=session['lastname'])
  


"""Once last question is completed print the quiz"""
@app.route("/solar_quiz/username/quiz_completed", methods=["GET", "POST"])
def quiz_completed():
    if session['score'] == 20:
        flash("Thanks for playing {0}. You scored {1}/20. Well done, that is a perfect score! See yourself on the leaderboard.".format(session['username'], session['score']))
    elif session['score'] >= 15:
        flash("Thanks for playing {0}. You scored {1}/20. That's a great score! See where you stand on the leaderboard.".format(session['username'], session['score']))
    elif session['score'] <= 10:
        flash("Thanks for playing {0}. You scored {1}/20. That's a decent score! See where you stand on the leaderboard, or look at the info.".format(session['username'], session['score']))
    else:
        flash("Thanks for playing {0}. You scored {1}/20. Have a look at the leaderboard, or the Solar Info page if you'd like to learn more about the solar system.".format(session['username'], session['score']))
    return render_template("quiz-completed.html", page_heading="Quiz Completed", username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score']) 
    
   
    
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
