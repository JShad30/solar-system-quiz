import json

"""Calling the data from questions.json and putting it into a variable called questions"""
questions = []
with open("data/questions.json", "r") as json_data:
    questions = json.load(json_data)

"""Creating a variable called score and setting it to 0"""
score = 0

"""function to loop round the questions in questions.json"""
def print_question(score):
      
    """Iterate round the questions printing the question and choices"""  
    for question in questions:
        print(question["question"])
        print(question["choices"][0])
        print(question["choices"][1])
        print(question["choices"][2])
        """Waiting for answerinput from user and checking whether this is the same as 'answer' in questions.json"""
        answer_given = input("Type your answer: ")
        if answer_given.lower() == question["answer"].lower():
            """If the same add one to the score"""
            score += 1
        print(score)
    
    """Ask the user for their names"""    
    first_name = input("Type your first name: ")
    last_name = input("Type your last name: ")
    
    """Check what value of score is and print message according to it."""    
    if score == 20:
        print("Congratulations {}! That's a perfect score!".format(first_name))
    elif score < 20 and score >= 15:
        print("You scored {}/20. Well done {}. That's a very good score".format(score, first_name))
    elif score < 15 and score >= 10:
        print("You scored {}/20. Thanks for playing {}. That's not a bad score".format(score, first_name))
    else:
        print("Thanks for playing {}. You scored {}/20. Be sure to check out the solar system info page.".format(first_name, score))

"""Run the function"""    
print_question(score)