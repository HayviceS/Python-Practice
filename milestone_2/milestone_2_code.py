#Getting info on the user
print("The information you put in will be stored, if you do not want this do not answer the questions.")
waking_up = int(input("What time do you wake up on a normal day: "))
age = int(input("How old are you: "))

if age > 0 and age <= 2:
    print("Are you allowed to be online? Oh well, you should be getting 12 - 17 hours of sleep per day, the younger you are the more you should sleep!")
elif age >= 3 and age <= 5:
    print("Your still growing and need a lot of sleep, 10 - 13 hours a day to be specific.")
elif age >= 6 and age <= 13:
    print("I know you probably want to stay up late, but you should be getting at least 9 hours of sleep and a maximum of 12 hours!")
elif age >= 14 and age <= 18:
    print("Your teen years are hard but a good night sleep can help with that! Try getting 8 - 10 hours of sleep a night")
elif age >= 19 and age <= 125:
    print("To be a healthy adult you need to be getting 7 - 9 hours of sleep. This ")
elif age <= 126:
    print("I find that hard to believe, but you should still be getting 7 - 9 hours of sleep a night.")
else:
    print("You can't be that old!")