#create a list with the possible outcomes of a fair dice
#create a program that roles the dice 
#the program should ask if the outcome is the value we want
# #create a conditional statement that will reroll the dice if its not our desired value but end if it is the value we want  
#make it 10 trials such that after the tenth trial and the sum of the first and secon roll is not eval to 10 the player has lost
#do a while loop for different conditiomn and if conditions are met an action should be performed
import random
choice_c = str(input ("press play to play again or end to end game; ").lower())
possible_Outcome= [1,2,3,4,5,6]
if choice_c == "play" :
        firstroll= random.choice(possible_Outcome)
        Secondroll= random.choice(possible_Outcome)
        print(f"{firstroll} and {Secondroll}")

elif choice_c=="end":
        print("Thank you for playing")
else:
        print("wrong syntax")



    #Number guessing Game 
    #the program should p[ick a number at randon
    #the program should ask us to input a number 
    #then if the nuber program picked is equal to the number i picked it should print you win
    #else it shpuld print you lose try again
    #then i shpould select yes or no if i want to try again
   

Computer_Num = random.randint(0,100)
while True:
    try:
        guess= int(input("guess a random number: "))
        if Computer_Num == guess:
            print("you win!!")
            break
        elif Computer_Num > guess:
            print("you coould have gone higher")
        else:
            print(" ouch try again later ") 
    except ValueError:
        print("Enter a valid number")