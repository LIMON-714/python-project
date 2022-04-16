name= input("type your name : ")
print("Welcome", name,"to this Adventure! ")

answer= input("you are one the road, it has come to end and you can go left or right. which you like to go? right now: ").lower()

if answer =="left":
    answer= input("you come to a river , you can walk around it or you can swim accross ? Type walk to walk around and swim to swim accross : ")

    if answer=="swim":
        print("You swim accross and were eaten by an allgator! ")

    elif answer=="walk":
        print("You walk for many miles , run out of water and lost The Game!")

    else:
        print("Not a valid option.")

elif answer == "right":
    answer= input("you come to a bridge ,it looks wobbly , what do you want to cross it or back? (cross/back)  :")

    if answer=="back":
        print("You can go back in the main road , now you can decide to drive ")

    elif answer=="cross":
        answer=input("You can cress the bridge and meet the stanger cant you do (yes/no)!  : ")

        if answer == "yes":
            print("!you talk to the stanger and get gold gift// ")

        elif answer == "no":
            print("You ignore the stanger and lost The Game!")

        else:
            print("Not a valid option.")


    else:
        print("Not a valid option.")


else:
    print("Not a valid option. you lose")


print("Thank you for trying mr/mst",name)