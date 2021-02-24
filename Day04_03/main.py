import random 
tie=0
my_choice=3

while my_choice not in (0,1,2):
    my_choice=int(input("enter your choice - 0 for Rock ; 1 for Paper ; 2 for Sciccors:"))
comp_input=random.randint(0,2)

print(f"You chose:{my_choice}")
print(f"Computer chose:{comp_input}")

if (my_choice==comp_input):
    print("You're tied! Pls play again!")
    exit()

if (my_choice==0):
    if(comp_input==1):
        you_win=0
    else:
        you_win=1
elif(my_choice==1):
    if(comp_input==2):
        you_win=0
    else:
        you_win=1
else:
    if(comp_input==0):
        you_win=0
    else:
        you_win=1

if you_win==0:
    print("You Lose!")
else:
    print("Yay!! You win!!")

    



