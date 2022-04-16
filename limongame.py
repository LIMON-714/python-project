print("welcome my quiz game!")

plying= input("do you want to play :  " )

if plying.upper()!="YES":
    quit()
print("Ok ! let's play : )")
score = 0
answer= input("what dose CPU stand for : ")
if answer.upper()=="CPU":
    print("correct! ")
    score += 1
else:
    print("Incorrect! ")

answer= input("what dose GPU3 stand for : ")
if answer.upper()=="GPU-3":
    print("correct! ")
    score += 1
else:
    print("Incorrect! ")

answer= input("what dose PSC5 stand for : ")
if answer.upper()=="PSC-55":
    print("correct! ")
    score+=1
else:
    print("Incorrect! ")

print("You got " +str(score)+ "questions correct! " )
print("Mark is " +str((score/4)*100)+ "%" )
print("The Game Is Over !")

