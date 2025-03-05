import random
print("winng rule of the Rock Paper Scissors games: \n Rock vs Paper : Paper wins \n Rock vs Scissors : Rock wins \n Paper vs Scissors : Scissors wins \n ")
computer_choice = random.choice([ 1 , 2 , 3 ])

your_choice = int(input("Enter your your_choice:\n 1 - rock , 2 - paper , 3 - siccors: "))

print(f"coumputer your_choice = {computer_choice}")
print(f"your_choice = {your_choice}")

if computer_choice == your_choice:
    print("draw")
else:
    if computer_choice == 1 and your_choice == 2:
        print("you wins")
    elif computer_choice == 1 and your_choice == 3:
        print("computer_choice wins")
    elif computer_choice == 2 and your_choice == 1:
        print("computer_choice wins")
    elif computer_choice == 2 and your_choice == 3:
        print("you wins")
    elif computer_choice == 3 and your_choice == 1:
        print("you wins")
    elif computer_choice == 3 and your_choice == 2:
        print ("computer_choice wins")
    else:
        print("You have Entered the wrong choice 'GAME FINISH' ")                       