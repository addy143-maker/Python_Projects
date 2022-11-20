#import random module first 
import random
import sys
from tkinter.messagebox import NO 

#print multiline instruction 
#performstring concatenation of string 
print("Winning rule of game rock,paper,scissor are as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                +"Rock vs scissor->Rock wins \n"
                                +"paper vs scissor-> scissor wins\n")

while True:
    
    print("Enter choice \n 1 for Rock, \n 2 for paper , and \n 3 for scissor \n")

    #add function to take input from user 
   
    choice = int(input("User turn: "))
   
    # OR is the short-cicuit operator 
    #if any one of the condition is true 
    #then it return true value 

    #adding loop function until the user enter the invalid input 
    while choice > 3 or choice < 1:
        choice = int(input("enter the valid input: ")) 

  
     # initialize value of choice_name variable 

     # corresponding to the choice value 
    if choice == 1:
           
         choice_name = 'Rock'

    elif choice == 2:

           choice_name = 'paper'

    else :
            choice_name = 'scissor'

    
    #print user choice
    print("user choice is: " + choice_name)
    print("\nNow its computer turn......")

    

    #computer chooses randomly any number 
    # among 1 , 2, and 3 using randit method 
    #of random module 

    comp_choice = random.randint(1 , 3)
  
#looping until comp_choice value is equal to the user value
    
     #while comp_choice == choice :
    
     #comp_choice = random.randint(1, 3)

    #initialize value of comp_choice_name 
    #variable corresponding to the choice view 

    if comp_choice == 1:

        comp_choice_name = 'Rock'

    elif comp_choice == 2:

        comp_choice_name = 'paper'

    else :
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

 # chech wheather its draw or not 
  
    if choice == comp_choice:

        print("Draw=> ",end = "")

    else:

        result = "Draw"

  

    # condition for winning 

    if((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
                print("paper wins =>", end = "")
                result = "paper"
            

    elif((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
                print("Rock wins =>", end = "")
                result = "Rock"

    else:
                print("scissor wins =>", end = "")
                result = "scissor"

        # print either user win or computer wins
    if result == "Draw":
             print(" <== Its A Tie ==> ")
    if result == choice_name:
            print("<== You win ==>")
    else :
            print("<==You loose ==>")

    print("Do you want to play again ? (Yes/No)")
    ans = input().lower

        #If user put n or N then condition is true 
    ans = "No"
    if ans == 'No':
        sys.exit("Thank for playing.")
        break
    elif ans == 'Yes':
        #restart_program ???
    
        print("\nThank for playing")




