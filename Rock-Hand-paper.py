# #Rock Hand paper
import random
import pandas as pd
def RockHandPaper():
    win= 0
    lose=0
    tie= 0
    result=["Win","lose","Tie"]
    list_x=["rock","paper","scissors"]
    
    while True :
        print("rock, paper, scissors,shoot!! or exit" )
        userhand=input("shoot!!>> ")
        comhand=random.choice(list_x)
        if userhand == "exit":
            print("Thank you for playing! Your score is")
            score=[win,lose,tie]
            df=pd.DataFrame (score,result)
            print(df)
            break
        if(comhand == userhand):
            print("Tie :D ")
            print(f"Computerhand shoot! {comhand}")
            tie+=1
        elif(comhand =="rock" and userhand=="paper"):
            print("You Win : ) ")
            print(f"Computerhand shoot! {comhand}")
            win+=1
        elif(comhand=="scissors" and userhand=="paper"):
            print("You lose : ( ) ")
            print(f"Computerhand shoot! {comhand}")
            lose+=1
        elif(comhand=="paper" and userhand=="scissors"):
            print("You Win : ) ")
            print(f"Computerhand shoot! {comhand}")
            win+=1
        elif(comhand=="rock" and userhand=="scissors"):
            print("You lose : ( ) ")
            print(f"Computerhand shoot! {comhand}")
            lose+=1
        elif(comhand=="scissors" and userhand=="rock"):
            print("You Win : ) ")
            print(f"Computerhand shoot! {comhand}")
            win+=1
        elif(comhand=="peper" and userhand=="rock"):
            print("You lose : ( ) ")
            print(f"Computerhand shoot! {comhand}")
            lose+=1
        else:
            print("Please try again shoot only rock,scissors,pape")
