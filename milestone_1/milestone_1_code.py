#Collecting info
name = input("What is your name?")
age = int(input("How old are you?"))
color = input("What's your favorite color?")

#Doubling age
double_age = 2
double_age *= age


#Printing info
print("Hi {}, you are {} when you double your age and your favorite color is {}.".format(name, double_age, color))