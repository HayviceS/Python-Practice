from datetime import datetime, timedelta
#Getting info on the user
print("The information you put in will be stored, if you do not want this do not answer the questions.")
waking_up = input("What time do you wake up on a normal day?(HH:MM in 24-hour format): ")
age = int(input("How old are you? "))

wake_time = datetime.strptime(waking_up, "%H:%M")

#Calculating
if age > 0 and age <= 2:
    min_sleep, max_sleep = 11, 14
elif age >= 3 and age <= 5:
    min_sleep, max_sleep = 10, 13
elif age >= 6 and age <= 13:
    min_sleep, max_sleep = 9, 12
elif age >= 14 and age <= 18:
   min_sleep, max_sleep = 8, 10
elif age >= 19 and age <= 125:
    min_sleep, max_sleep = 7, 9
elif age >= 126:
    print("I find that hard to believe, but you should be getting 7 - 9 hours of sleep a night.")
    min_sleep, max_sleep = 7, 9
else:
    print("You can't be that old!")

earliest_bedtime = (wake_time - timedelta(hours=max_sleep)).time()
latest_bedtime = (wake_time - timedelta(hours=min_sleep)).time()

#Output 
print(f"Based on the information given, your age ({age}) and the time you wake up ({waking_up}) you should go to bed between {earliest_bedtime.strftime('%H:%M')} and {latest_bedtime.strftime('%H:%M')}.")