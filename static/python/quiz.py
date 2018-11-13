import json

questions = []
with open("data/questions.json", "r") as json_data:
    questions = json.load(json_data)

score = 0

def print_question(score):
        
    for question in questions:
        print(question["question"])
        print(question["choices"][0])
        print(question["choices"][1])
        print(question["choices"][2])
        answer_given = input("Type your answer: ")
        if answer_given.lower() == question["answer"].lower():
            score += 1
        print(score)
        
    first_name = input("Type your first name: ")
    last_name = input("Type your last name: ")
        
    if score == 20:
        print("Congratulations {}! That's a perfect score!".format(first_name))
    elif score < 20 and score >= 15:
        print("You scored {}/20. Well done {}. That's a very good score".format(score, first_name))
    elif score < 15 and score >= 10:
        print("You scored {}/20. Thanks for playing {}. That's not a bad score".format(score, first_name))
    else:
        print("Thanks for playing {}. You scored {}/20. Be sure to check out the solar system info page.".format(first_name, score))
    
print_question(score)