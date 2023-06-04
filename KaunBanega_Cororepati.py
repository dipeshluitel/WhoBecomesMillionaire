# source = https://www.edudwar.com/world-gk-quiz-questions-and-answers/
questions = ["Which is the Smallest ocean?", "Which country gifted 'Statue of Liberty' to USA", "Which Country is also known as 'Land of Rising Sun'?","Which Continent has the highest number of countries?", "Total number of ocean in the world is?","Which is one of the biggest island?","The world's longest straight road without any corners is located in?","Which one is the largest tropical rain forest in the world?","Which country is known as 'Land of Thousands Lakes'?","In which country, white elephant is found?"]
ans=["Arctic","France","Japan","Africa","5","Greenland","Saudi Arabia","Amazon","Finland","Thailand"]
name=input("Enter your name:")
amount=0
result= "T"
command=input("press y to start and n to abort:")
if(result=="T"):
    match command:
        case "y":
                pass
        case "n":
                print(name,"You have won:",amount)
                print("Thank you for playing".center(50,"."))
                result="F"
    