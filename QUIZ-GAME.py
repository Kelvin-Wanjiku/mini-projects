print("welcome to my computer quiz")
playing = input("Do you want to play this game? ").lower()
if playing!="yes" :
    quit()
    
print("welcome to the game")

score=0

answer= input("what does the cpu stand for? ").lower()
if answer == "central processing unit":
     print("correct!")
     score+=1

else:
    print("incorrect")


answer= input("what does the GPU stand for? ").lower()
if answer == "graphic processing unit":
     print("correct!")
     score+=1

else:
    print("incorrect")


answer= input("what does the RAM stand for? ").lower()
if answer == "random access memory":
     print("correct!")
     score+=1

else:
    print("incorrect")

print("you scored " + str(score) + " out of three")    

percentage= (score/3)*100
print("percentage score")
print(percentage)
