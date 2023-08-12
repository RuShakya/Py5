print("Welcome to my Computer quiz")

# Making a Quiz Game

playing = input ("Do you want to play ??")

if playing.lower() != "yes":
    quit()                  # quits the program

print("Okay! Let's Playyy")
score = 0                   # to track the score of the correct answers 


answer = input(" What does CPU stands for? ")
if answer.lower() == "central processing unit":             # .lower() to make the program read in lower case (program will automatically convert it into lower case)
    print("Correct!")                                       # but the one written in double code "...." must be in lower case
    score += 1              # score increment 
else:
    print("Incorrect!")


answer = input(" What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1              # score increment 
else:
    print("Incorrect!")


answer = input(" What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1              # score increment 
else:
    print("Incorrect!")


answer = input(" What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1              # score increment 
else:
    print("Incorrect!")


print ("You got " +  str(score)  + " questions correct!")         # score stored in string to join in that sentence
print ("You got " + str((score/4)*100) +    "%")                  # for percentage



# end of first mini project