print("Welcome to my Computer quiz")

# Making a Quiz Game

playing = input ("Do you want to play ??")

if playing != "yes":
    quit() 

print("Okay! Let's Playyy")

answer = input(" What does CPU stands for? ")
if answer == "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect!")


answer = input(" What does RAM stands for? ")
if answer == "Random Access Memory":
    print("Correct!")
else:
    print("Incorrect!")

