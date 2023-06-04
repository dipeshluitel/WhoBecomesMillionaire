# source = https://www.edudwar.com/world-gk-quiz-questions-and-answers/
questions = ["Which is the Smallest ocean?\na.Indian\t\tb.Pacific\nc.Atlantic\t\td.Arctic", "Which country gifted 'Statue of Liberty' to USA?\na.France\t\tb.Canada\nC.Brazil\t\td.England", 
             "Which Country is also known as 'Land of Rising Sun'?\na.Japan\t\tb.New Zealand\nc.Fiji\t\tc.China", "Which Continent has the highest number of countries?\na.Asia\t\t\tb.North America\nc.Europe\t\td.Africa", 
             "Total number of ocean in the world is?\na.3\t\tb.5\nc.7\t\td.12","Which is one of the biggest island?\na.Borneo\t\tb.Finland\nc.Sumatra\t\td.Greenland", 
             "The world's longest straight road without any corners is located in?\na.USA\t\t\tb.Australia\nc.Saudi Arabia\t\td.China", "Which one is the largest tropical rain forest in the world?\na.Amazon\t\tb.Southeast Asian Rain Forest\nc.Bosawas\t\td.Daintree Rain Forest", 
             "Which country is known as 'Land of Thousands Lakes'?\na.Iceland\t\tb.Norway\nc.Finland\t\td.Switzerland", "In which country, white elephant is found?\na.India\t\t\tb.Sir Lanka\nc.Thialand\t\td.Malaysia"]
ans = ["d", "a", "a", "d", "b", "d", "c", "a", "c", "c"]
nam = input("Enter your name:")
name=nam.upper()
amount = 0
result = "T"
command = input("press y to start and n to abort:")
if (result == "T"):
    match command:
        case "y":
            temp = "t"
            for i in range(10):
                if ("temp=t"):
                    # print(name,"Total win:",amount)
                    print(i+1, questions[0+i])
                    ret = input("Enter the option:")
                    ret.lower()
                    if (ret.lower() == ans[0+i]):
                        amount = amount+100000
                        print("Congratulation", name, "you have won:", amount)
                        wish = input("Do you wish to continue playing y or n:")
                        if(i==9):
                            print(name, "your total win is:", amount,"You are CROREPATI")
                            print("Thankyou for Playing".center(50, "-"))
                            break
                        elif (wish.lower() == "y"):
                            pass
                        else:
                            print(name, "You have won:", amount)
                            print("Thank you for playing".center(50, "."))
                            print(":".center(50, "."))
                            break

                    else:
                        print("The option which you have entered is wrong".center(50, "/"))
                        print(name, "your total win is:", amount)
                        print("Thankyou for Playing".center(50, "-"))
                        break

        case "n":
            print(name, "You have won:", amount)
            print("Thank you for playing".center(50, "."))
            result = "F"
        case __:
            print("Invalid Input")
