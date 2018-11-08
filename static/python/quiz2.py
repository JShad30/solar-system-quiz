from flask import Flask, redirect, render_template, request
import json


    
    score = 0
  
    data = []
    
    with open("data/questions.json", "r") as json_data:
        data = json.load(json_data)
    q = data[0]["question"]
    c = data[0]["choices"]
    question_list=data
    
    for question in question_list:
        return question
        
    def solar_system_quiz():    
        
if __name__ == '__main__':
    solar_system_quiz()