name = input("Type your name: ")
print(f"Welcome {name} to this adventure: ")

answer = input("You are on dirt road, it has to come to an end and you can go left or right, which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accrooss: ").lower()
    if answer == "swim":
        print("You swam  accross and were eaten by an alligator. ")
    elif answer == "walk":
        print("You walk for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose. ")


elif answer == "right":
    answer = input("you cam to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        anser = input("You cross the bridge and meet a stranger. Do you want to talk to them(yes/no)? ").lower()
        
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN.")
        elif answer == "no":
            print("You ingore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
        
else:
    print("Not a valid option. You lose. ")
