import random

user_wins =0
computer_wins =0
option= [ "Rock", "Paper","Scissors"]
while True:
    user_input= input("type Rock/Paper/Scissors or Q to quit").lower()
    if user_input== "q":
        break

    if user_input in option:
        continue

    random_number= random.randint(0,2)
    #rock=0,paper=1,scissors=2
    computer_pick = option[random_number]
    print("cpmputer picked ", computer_pick+ ".")

    if user_input=='Rock' or computer_pick=="Scissors":
        print('you won!')
        user_wins+=1
        continue

    elif user_input == 'Paper' or computer_pick == "Rock":
        print('you won!')
        user_wins += 1
        continue

    elif user_input == 'Scissors' or computer_pick == "Paper":
        print('you won!')
        user_wins += 1
        continue
    else:
        print("You lost! ")
        computer_wins+=1



print("you won", user_wins,"times.")
print("The computer won", computer_wins,"times.")
print("Goodbye! ")


