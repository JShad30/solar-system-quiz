import os
import json
import csv
from flask import Flask, url_for, render_template, request, redirect, flash, session
import ast

app = Flask(__name__)
app.secret_key = "username_collected"



"""Calling the data from questions.json and putting it into a variable called questions"""
questions = []
with open("data/questions.json", "r") as json_data:
    questions = json.load(json_data)
    
    
    
"""def write_info_to_names(path, filename, data):
    filename = "data/names.json"
    with open(filename, 'a') as results:
        json.dump(player, results)"""



"""Rendering the home page"""
@app.route("/")
def index():
    session.clear()
    return render_template("index.html", page_heading="Welcome")
  
  
  
"""Rendering the solar info page"""   
@app.route("/solar_info")
def solar_info():
    session.clear()
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
        #Set the score variable to be used in get_question to 0
        score = 0
        
        """Creating the sessions for the variables"""
        session['username'] = username
        session['firstname'] = firstname
        session['lastname'] = lastname
        session['score'] = score
        """Setting the Variables"""
        flash("Thanks for playing {0}. Your username is {1}, so be sure to look for it on the leaderboard at the end".format(request.form["firstname"], request.form["username"]))
        return render_template("solar-quiz-user.html", page_heading="Solar System Quiz", username=username, firstname=firstname, lastname=lastname)
        
    return render_template("solar-quiz.html", page_heading="Solar System Quiz")



"""Iterating through the questions from the solar-bodies-info.json file"""    
@app.route("/solar_quiz/<username>/question/<int:id>", methods=["GET", "POST"]) #How to put the button in this part of the file to iterate through the questions?
def get_question(username, id):
    questions = []
    print(request.form.items()) #Mentor suggestion to show in console below
    with open("data/questions.json", "r") as json_data:
        questions = json.load(json_data)
        q = questions[id - 1]["question"]
        c = questions[id - 1]["choices"]
        a = questions[id - 1]["answer"]
        for q in questions:
            if request.method == "POST":
                answer_given = request.form["choice"] #Variable answer_given finds which was selected in questions.py
                """function to increase value of score by 1 if correct_answer is the same as answer_given"""
                #def add_score(score, a): #create the function with score as an argument - currently set at 0
                if answer_given.lower() == a.lower(): #Check whether answer given and correct answer are the same
                    session['score'] += 1 #if so add 1
                print(answer_given.lower())
                print(a.lower())
                print(session['score'])
                #return score #Return the final score when all answers added together
                id += 1
                if id > 5:#len(questions):
                    return redirect(url_for("quiz_completed", page_heading="Quiz Completed", username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score']))
                return redirect(url_for("get_question", username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score'], id=id))
                
            return render_template("questions.html", page_heading="Quiz Questions", question=questions[id - 1], username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score'], id=id)
  


"""Once last question is completed print the quiz"""
@app.route("/solar_quiz/quiz_completed", methods=["GET", "POST"])
def quiz_completed():
    names = {}
    names['username'] = session['username']
    names['firstname'] = session['firstname']
    names['lastname'] = session['lastname']
    names['score'] = str(session['score'])
    
    with open('data/names.txt', 'a') as names:
        #json.dump(names, player, ensure_ascii=False, indent=4)
        names.writelines('{"username": "' + session['username'] + '", "firstname": "' + session['firstname'] + '", "lastname": "' + session['lastname'] + '", "score": "' + str(session['score']) + '"}' + '\n')

    if session['score'] == 20:
        flash("Thanks for playing {0}. You scored {1}/{2}. Well done, that is a perfect score! See yourself on the leaderboard.".format(session['username'], session['score'], len(questions)))
    elif session['score'] >= 15:
        flash("Thanks for playing {0}. You scored {1}/{2}. That's a great score! See where you stand on the leaderboard.".format(session['username'], session['score'], len(questions)))
    elif session['score'] >= 10:
        flash("Thanks for playing {0}. You scored {1}/{2}. That's a decent score! See where you stand on the leaderboard, or look at the info.".format(session['username'], session['score'], len(questions)))
    else:
        flash("Thanks for playing {0}. You scored {1}/{2}. Have a look at the leaderboard, or the Solar Info page if you'd like to learn more about the solar system.".format(session['username'], session['score'], len(questions)))
    return render_template("quiz-completed.html", page_heading="Quiz Completed", username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score'])
    
   
    
"""Post quiz leaderboard rendering"""
@app.route("/solar_quiz/leaderboard")
def leaderboard():
    names_list = []
    with open('data/names.txt') as player_names:
        names = player_names.read().splitlines()
        
    """Following two lines suggested by tutor and ast imported"""
    for n in names:
        names_list.append(ast.literal_eval(n))
    print(names_list)
    
    return render_template("leaderboard.html", page_heading="Current Leaderboard", player_names=names_list)



"""Running the functions and rendering pages from above"""
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
