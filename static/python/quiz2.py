from flask import Flask, redirect, render_template, request
import json

score = 0

def get_question(id):
    data = []
    with open("data/questions.json", "r") as json_data:
        data = json.load(json_data)
    q = data[id]["question"]
    c = data[id]["choices"]

    for single_question in data:
        print(q.question)
        print(c.choices[0])
        print(c.choices[1])
        print(c.choices[2])
        answer_given = input("Type your answer: ")
        def calc_score():
            if answer_given.lower() == single_question.answer:
                score += 1

if __name__ == '__main__':
    get_question(id)