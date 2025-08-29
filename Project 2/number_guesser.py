import random
name = input("Enter your name: ")

for i in range(len(name)):
    if name[i].isdigit():
        print("Don't ENTER DIGITS IN NAME!")
        quit()
    
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time. ")
        quit()

else:
    print("Please type a number next time.")

random_number = random.randint(0, top_of_range)

guesses = 0 
while True:
    guesses +=1 
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print(f"{name}!Please type a number next time.")
        continue

    if user_guess == random_number:
        print(f"You got it! {name}")
        break
    
    elif user_guess < random_number:
        print(f"<-- Guess a higher number {name}-->")
    else:
        print(f"<-- Guess a lower number {name} -->")


print(f"You got it in {guesses} times.")