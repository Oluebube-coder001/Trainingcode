import random


print("Winning rules of the Rock, Paper and Scissors game are as follows: \n" + "Rock vs Paper --> Paper wins \n" + "Rock vs Scissors --> Rock wins \n" + "Paper vs Scissors --> Scissors wins \n")

while True:
    print("Enter choice \n 1 for Rock, \n 2 for Paper, and \n 3 for Scissor \n")
    
    choice = int (input("User turn: "))
    
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
        
        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = "Paper"
        else:
            choice_name = "Scissor"
            
        print ("user choice is: " + choice_name)
        print("\n it's my turn now.........")
        
        comp_choice = random.randint(1, 3)
        
    while comp_choice == choice:
        comp_choice == random.randint(1, 3)
        
        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name ='Paper'
        else:
            comp_choice_name = 'Scissor'
        print("Computer choice is: " + comp_choice_name)
        print(choice_name + "V/s " + comp_choice_name)
        
        if choice == comp_choice:
            print("Draw=> ", end = " ")
            result = Draw
            
        if((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
            print("paper wins => ", end = "")
            result = "Paper"
        elif ((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
            print("Rock wins =>", end = " ")
            result = "Rock"
        else:
            print("Scissor wins =>", end = "")
            result = "Scissor"
            
    if result == Draw:
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== You Win :) ==>")
    else:
        print("<== I won ==>")
        
    print("Do you want to play again? (Y/N) ")
    ans = input().lower
    
    if ans == 'n':
        break
    
    print("\nThanks for playing:)")
            