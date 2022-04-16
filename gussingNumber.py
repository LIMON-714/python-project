from random import randint



plying= input("do you want to play?...... :  " )

if plying.upper()!="YES":
    print("Game Is Over//")
    quit()


print("Ok ! let's play : )")
score = 0
for x in range(1,11):

    gussNumber = int(input("   Enter any gussing number as you like : "))
    randomNumber = randint(1,2)
    if randomNumber == gussNumber:
        print("                  The gussNumber is correct !")
        score += 1
    else:
        print("                  The gussNuber is not correct try again!")

    print("                               ........The random number is  (..",randomNumber,"..)")

print("\n")

print("                                   You got " +str(score)+ "questions correct! " )
print("                                         Mark is " +str((score/10)*10)+ "%" )
print("---------------------------------------The Game Is Over !----------------------------------------")