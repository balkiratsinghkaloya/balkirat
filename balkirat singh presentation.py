print("Welcome to my computer quiz!")
playing = input("do you want to play?")

if playing !="yes":
    quit()

print("Okay! let's play :-)")
print("this is round one answer either true or false") 
print(" 1 Tiger is our national animal")
a=input()
if a =="true":
    print('conratulations,your answer is correct')
    score =+ 1 
else:
        print("False,correct answer is tiger")
print("2 Cricket is our national sport")
a=input()
if a=="false":
    print("congratulations,your answer is correct Hockey is our national sport")
    score =+ 1
else:
        print("incorrect,hockey is our national sport")
print("3 Peackock is our national bird")
a=input()
if a=="true":
    print("conratulations,your answer is correct")
    score =+ 1
else:
    print('incorrect')
    print("round two stars answer either true or false")
    print("1 The earth is round")
a=input()
if a=="true":
    print("congratulations,your answer is correct")
    score =+ 1
else:
    print("your answer is incorrect")
print("2 RAM stands for random access memory")
a=input()
if a=="true":
    print("congratulations,your answer is correct")
    score =+ 1
else:
    print("yor answer is incorrect")  
    print("round two overs")
    print("round three starts answer either true or false") 
    print("1 sharks are mammals")
a=input()
if a=="false":
    print("congratulations,your answer is correct")
    score =+ 1
else:
    print("incorrect,sharks are classified as fish")

    print("2 Bats are blind")
a=input()
if a=="false":
    print("congratulations,your answer is correct")
    score =+ 1
else:
    print("incorrect they have eyes")

    print("round 3 overs")
    print("round four begins")
    print("1 Dogs have four legs")
a=input()
if a=="true":
    print("congratulations,your answer is correct")
    score =+ 1
else:
    print("incorrect answer")
    
print("2 Fish lives in water")
a=input()
if a=="true":
    print("congratulations,your answer is correct")
    score =+ 1
else:
    print("incorrect answer")  

    print("round 4 overs ")
    print("round 5 last round begins answer either true or false")
    print(" 1 America is largest country in terms of area")
a=input()
if a=="false":
    print("congratulations,your answer is correct")
    score =+ 1
else:
    print("incorrect russia is largest") 
    print(" 2 Gujrat has the longest coastine in india")   
a=input()
if a=="false":
    print("congratulations,your answer is correct")
    score =+ 1
else:
    print("incorrect adaman nicobar has the longest ")
    print("You got" + str(score) + "questions correct!")
    print("You got" + str((score/4)*100) + "%." )
