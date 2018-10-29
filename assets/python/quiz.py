question_one = "1. Which planet is nearest to the sun?\na. Venus\nb. Mercury\nc. Pluto\nType the letter of your answer"
question_two = "2. What is the largest planet in the solar system?\na. Jupiter\nb. Uranus\nc. Saturn\nType the letter of your answer"
question_three = "3. Between which two planets do you find the asteroid belt?\na. Earth and Mars\nb. Mars and Jupiter\nc. Jupiter and Saturn\nType the letter of your answer"
question_four = "4. What is the name of the largest object in the asterid belt?\na. Ceres\nb. Juno\nc. Hygiea\nType the letter of your answer"
question_five = "5. Now pluto has been downgraded as a planet, which planet is the furthest from the sun?\na. Uranus\nb. Neptune\nc. Venus\nType the letter of your answer"
question_six = "6. How many planets are there?\na. Eight\nb. Six\nc. Seven\nType the letter of your answer"
question_seven = "7. How many of these are gas giants?\na. Five\nb. Three\nc. Four\nType the letter of your answer"
question_eight = "8. Umbriel is a moon of which planet?\na. Saturn\nb. Neptune\nc. Uranus\nType the letter of your answer"
question_nine = "9. How many moons orbit Mars?\na. One\nb. Two\nc. Three\nType the letter of your answer"
question_ten = "10. Which of these is a moon of Mars?\na. Makemake\nb. Europa\nc. Phobos\nType the letter of your answer"
question_eleven = "11. Pluto is the largest object in which part of the solar system?\na. Kuiper Belt\nb. Inner Planets\nc. Oort Cloud\nType the letter of your answer"
question_twelve = "12. Which of these is not one of Plutos moons?\na. Hydra\nb. Io\nc. Nix\nType the letter of your answer"
question_thirteen = "13. Which planet is famous for its large rings?\na. Venus\nb. Neptune\nc. Saturn\nType the letter of your answer"
question_fourteen = "14. Which of the planets is thought to have the warmest climate?\na. Mars\nb. Venus\nc. Mercury\nType the letter of your answer"
question_fifteen = "15. After the sun, which is the nearest star to the solar system at four light years?\na. Proxima Centauri\nb. Barnards Star\nc. Centauri A\nType the letter of your answer"
question_sixteen = "16. The solar system is a part of which galaxy?\na. The Sombrero Galaxy\nb. Andromeda\nc. Milky Way\nType the letter of your answer"
question_seventeen = "17. Approximately how old is the solar system thought to be?\na. 6 Billion Years\nb. 4.5 Billion Years\nc. 3 Billion Years\nType the letter of your answer"
question_eighteen = "18. When the moon passes across the sun and blocks the daylight, this is called a solar...\na. Eclipse\nb. Storm\nc. Flair\nType the letter of your answer"
question_nineteen = "19. Makemake is part of the asteroid belt. True or false?\na. True\nb. False\nc. There is no such object\nType the letter of your answer"
question_twenty = "20. Which of these is a comet?\na. Halley's\nb. Eris\nc. Callisto\nType the letter of your answer"

def solar_system_quiz():
        
    score = 0
    
    #Question one
    print(question_one)
    question_one_answer = input()
    if question_one_answer.lower() == "b":
        score += 1
    
    #Question two            
    print(question_two)
    question_two_answer = input()
    if question_two_answer.lower() == "a":
        score += 1
            
    print(str(score))

if __name__ == '__main__':
    solar_system_quiz()

