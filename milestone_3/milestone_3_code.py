# Intro
while True:
    print("Hi, are you ready to start a quiz about 'The Rookie'!")
    print("Your answers to these questions will be saved, do not continue if you are not okay with this.")

    #Start the game
    start = input("Would you like to start the game? yes/no: ")
    start.lower
    if start == "yes":
        print("Cool! Let's get started.")

        # Asking questions
        score = 0 
        question = "What American city is The Rookie based?"
        a = "Los Angeles"
        b = "New York"
        c = "Chicago"
        answer = input("{}\nA. {}  B. {}  C. {}\n".format(question, a, b, c)).lower()

        if answer == "a" or answer == a.lower():
            print("Correct!")
            score += 1
        elif answer == "b" or answer == b.lower() or answer == "c" or answer == c.lower():
            print("Incorrect.")
        else:
            print("That's not an answer, please pick A, B, or C.\n")
            
        question_2 = "What job did John Nolan have before becoming a cop?"
        a2 = "Paramedic"
        b2 = "Bank teller"
        c2 = "Construction worker"
        answer2 = input("{}\nA. {}  B. {}  C. {}\n".format(question_2, a2, b2, c2)).lower()

        if answer2 == "c" or answer2 == c2.lower():
            print("Correct!")
            score += 1
        elif answer2 == "b" or answer2 == b2.lower() or answer2 == "a" or answer2 == a2.lower():
            print("Incorrect.")
        else:
            print("That's not an answer, please pick A, B, or C.\n")
            
        question_3 = "Who is Lucy Chen's training officer?"
        a3 = "Tim Bradford"
        b3 = "Nyla Harper"
        c3 = "Wade Grey"
        answer3 = input("{}\nA. {}  B. {}  C. {}\n".format(question_3, a3, b3, c3)).lower()

        if answer3 == "a" or answer3 == a3.lower():
            print("Correct!")
            score += 1
        elif answer3 == "b" or answer3 == b3.lower() or answer3 == "c" or answer3 == c3.lower():
            print("Incorrect.")
        else:
            print("That's not an answer, please pick A, B, or C.\n")
                
        #Ending the quiz
        print("Good job! You made it to the end of the quiz! Your final score was {}/3".format(score))

    #Don't want to play
    if start == "no":
        exit = input("Are you sure? yes/no: ")
        if exit == "yes":
            print("That's ok. Come back if you change your mind!")
            break
            if exit == "no":
                print("Cool! Let's get started.")