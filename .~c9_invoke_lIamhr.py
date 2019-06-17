import os
import json
from flask import Flask, url_for, render_template, request, redirect, flash, session
"""from flask.ext.session import Session"""

app = Flask(__name__)
app.secret_key = "username_collected"
"""sess = Session()"""


"""Calling the data from questions.json and putting it into a variable called questions"""
questions = []
with open("data/questions.json", "r") as json_data:
    questions = json.load(json_data)



"""Rendering the home page"""
@app.route("/")
def index():
    session.clear() #Make sure no session exists when this page is accessed
    return render_template("index.html", page_heading="Welcome")
  
  
  
"""Rendering the solar info page"""   
@app.route("/solar_info")
def solar_info():
    session.clear() #Make sure no session exists when this page is accessed
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
        score = 0 #Set the score variable to be used in get_question to 0
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
    print('last -> session={} and id={}'.format(session, id))
    if id not in session and id > 1:
        return redirect(url_for("get_question", username=session['username'], id=1))
    if id in session and id < session['id']-1:
        return redirect(url_for("get_question", username=session['username'], id=session['id']-1))
    
    questions = []
    print(request.form.items()) #Mentor suggestion to show in console below
    print(request.form.items()) #Mentor suggestion to show in console below
        
        """Loading the questions, choices and answers from the questions json file"""
        questions = json.load(json_data)
        q = questions[id - 1]["question"]
        c = questions[id - 1]["choices"]
        a = questions[id - 1]["answer"]
        
        for q in questions:
            if request.method == "POST":
                answer_given = request.form["choice"] #Variable answer_given finds which was selected in questions.py
                """increase value of score by 1 if correct_answer is the same as answer_given"""
                if answer_given.lower() == a.lower(): #Check whether answer given and correct answer are the same
                    session['score'] += 1 #if so add 1
                """Check in terminal that answers given and answer were the same, and that score was being added correctly"""
                print(answer_given.lower())
                print(a.lower())
                print(session['score'])
                
                """Add one to id"""
                id += 1
                session["id"] = id
                if id > 3:
                    return redirect(url_for("quiz_completed", page_heading="Quiz Completed", username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score']))
                    
                return redirect(url_for("get_question", username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score'], id=id))
                
            return render_template("questions.html", page_heading="Quiz Questions", question=questions[id - 1], username=session['username'], firstname=session['firstname'], lastname=session['lastname'], score=session['score'], id=id)
            
            

"""Once last question is completed print the quiz"""
@app.route("/solar_quiz/quiz_completed", methods=["GET", "POST"])
def quiz_completed():
    names = {}
    
    #Setting variables for the data collected in the form and the score
    names['username'] = session['username']
    names['firstname'] = session['firstname']
    names['lastname'] = session['lastname']
    names['score'] = str(session['score'])
    
    """write the variables and the score to a dictionary"""
    with open('data/names.txt', 'a') as names:
        names.writelines('{"username": "' + session['username'] + '", "firstname": "' + session['firstname'] + '", "lastname": "' + session['lastname'] + '", "score": "' + str(session['score']) + '"}' + '\n')

    """If statement to work out score, and display correct message accordingly. Scores here worked out in percentages, so that extra questions can be added at any time without havig to rewrite the code."""
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
    session.clear() #Make sure no session exists when this page is accessed
    names_list = []
    with open('data/names.txt') as player_names:
        
        """Reading the names from the names.txt file"""
        names = player_names.read().splitlines()
    for n in names:
        
        """load the names in names dictionary as a json file"""
        names_list.append(json.loads(n))
    
    """Sorting the names on the leaderboard in score order."""
    names_list = sorted(names_list, key=lambda k: int(k['score']), reverse=True) #ast removed following discussion with mentor and dictionary converted to a json file so that the leaderboard can be ordered.
    print(names_list)
    
    return render_template("leaderboard.html", page_heading="Current Leaderboard", player_names=names_list)



"""Running the functions and rendering pages from above"""
if __name__ == "__main__":
    """sess.init_app(app)"""
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
