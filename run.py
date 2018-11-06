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
    
    
    """Main page with instruction"""
    #Handle the post request
    if request.method == "POST":
        write_to_file("static/data/names.txt", request.form["firstname" + "lastname"] + "\n")
        
        return redirect(request.form["firstname" + "lastname"])
    return render_template("solar-quiz.html")
    
@app.route("/<firstname><lastname>")
def user(firstname, lastname):
    """Display Name"""
    names = receive_input_names()
    return render_template("solar-quiz.html", firstname=firstname, lastname=lastname, new_players=names)



        
"""Writing the names of players to the data/names.txt file"""        
        
def write_to_file(filename, data):
    """Writing the data to the to file"""
    with open(filename, "a") as file:
        file.writenames(data)
        
def add_messages(firstname, lastname):
    """Add names to the list of names in the names.txt file"""
    write_to_file("data/messages.txt", "{0} {1}\n".format(
        firstname.title(),
        lastname.title()))        
        
def receive_input_names():
    """Get all of the names inputed from the quiz page and separate them by a `br`"""
    names = []
    with open("static/data/names.txt", "r") as add_name:
        names = add_name.readlines()
    return names



    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
