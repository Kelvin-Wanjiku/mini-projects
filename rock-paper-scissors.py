import random

user_wins =0
computer_wins =0
options= ["rock", "paper", "scissors"]

while True:
    user_input =input("rock/paper/scissors or Q to quit. ").lower()

    if user_input =="q":
        print("come back next time")
        break

    if user_input not in options :
        continue

    random_number = random.randint(0, 2)

    #rock=0 paper=1 scissors=2
    
        
    
