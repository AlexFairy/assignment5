#Task One

#Objective: 
import random

moods = ['happy', 'sad', 'energetic', 'calm']
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(len(week_days)): #loops through each data point in list as length
  print("Normally I feel " + random.choice(moods) + " on " + week_days[i] + "s")# The aim of this assignment is to deepen your understanding of Python's range() function.


#Example Outcome: 
# An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."

#2. Double Scoop with Nested Loops
#Objective: The aim of this assignment is to practice using nested loops in Python.
#Task 1: Your Mood Tracker

import random #Version 1

moods = ['happy', 'sad', 'energetic', 'calm']
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_day = ["morning", "afternoon", "evening"]

for i in range(len(week_days)):
  for x in range(3):
    print("Normally I feel " + random.choice(moods) + " on " + week_days[i] + "s in the " + time_day[x])


import random #Version 2

moods = ['happy', 'sad', 'energetic', 'calm']
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_day = ["morning", "afternoon", "evening"]

for i in range(len(week_days)):
  print("Normally I feel " + random.choice(moods) + " on " + week_days[i] + "s in the " + random.choice(time_day))

#Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) 
# for each day of the week. Use nested loops to implement this: 
# the outer loop should iterate over the days, and 
# the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.

#Example Outcome: 
# An example would be "On Tuesday afternoon you were sad" 
# "On Tuesday night you were happy" 
# "On Wednesday morning you were tired"