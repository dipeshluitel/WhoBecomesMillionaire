# source = https://www.edudwar.com/world-gk-quiz-questions-and-answers/
#Question For quiz
questions = [["Which is the Smallest ocean?", "Indian", "Pacific", "Atlantic", "Arctic", "d"],
             ["Which country gifted 'Statue of Liberty' to USA?", "France","Canada","Brazil","England","a"],
             ["Which Country is also known as 'Land of Rising Sun'?","Japan", "New Zealand", "Fiji","China","a"],
             ["Which Continent has the highest number of countries?","Asia", "North America", "Europe", "Africa","d"],
             ["Total number of ocean in the world is?","3", "5", "7", "12","b"],
             ["Which is one of the biggest island?","Borneo", "Finland", "Sumatra","Greenland","d"],
             ["The world's longest straight road without any corners is located in?","USA", "Australia", "Sauid Arabia", "China","c"],
             ["Which one is the largest tropical rain forest in the world?","Amazon", "South East Asia Rainforest", "Bosawas","Daintree Rain Forest", "a"],
             ["Which country is known as 'Land of Thousands Lakes'?","Iceland", "Norway", "Finland", "Switzerland","c"],
             ["In which country, white elephant is found?","India", "Sirlanka", "Thailand", "Malaysia","c"]]


#Details about players
nam = input("Enter your name:")
name = nam.upper()
amount = 0

#START

command = input("press y to start and n to abort:")
match command:
    case "y":
        temp = "t"
        for i in range(10):

            #Inorder to access the lists of list
            question = questions[i]
            if ("temp=t"):
                
                    #Question and Options Displays here
                    print(i+1,f"{question[0]}")
                    print(f"a.{question[1]}                             b.{question[2]}")
                    print(f"c.{question[3]}                             d.{question[4]}")
                    ret = input("Enter the option:")
                    ret.lower()

                    
                    #IF CORRECT ANSWER IS ENTERED
                    if (ret.lower() == question[5]):
                        amount = amount+100000
                        print("Congratulation", name, "you have won:", amount)
                        print(":".center(50, "."))
                        if (i == 9):
                            print(name, "your total win is:",amount, "You are CROREPATI")
                            print("Thankyou for Playing".center(50, "-"))
                            break
                    #IF WRONG ANSWER IS ENTERED
                    else:
                        print("The option which you have entered is wrong".center(50, "/"))
                        print(name, "your total win is:", amount)
                        print("Thankyou for Playing".center(50, "-"))
                        break    
                    
                    #To Check if the User wants to Continue Playing or not
                    wish = input("Do you wish to continue playing y or n:")
                    if (wish.lower() == "y"):
                        pass
                    else:
                        print("Thank you for playing".center(50, "."))
                        print(name, "You have won:", amount)
                        print(":".center(50, "."))
                        break

            else:
                print("Thank you for playing".center(50, "."))
                print(name, "You have won:", amount)
                print(":".center(50, "."))
                break

               


    case "n":
        print(name, "You have won:", amount)
        print("Thank you for playing".center(50, "."))
        result = "F"
    case __:
        print("Invalid Input")
