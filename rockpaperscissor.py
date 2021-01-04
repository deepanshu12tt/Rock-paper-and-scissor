import random
root=Tk()
root.title("Rock, paper and scissor game")
root.geometry("600x500")
Button(root,text="Rock",command=rock).pack()
Button(root,text="paper",command=paper).pack()
Button(root,text="Scissor",command=scissor).pack()
root.mainloop()
choice=["Rock","Paper","Scissor"]       ##list where to choose from
while True:
    print("Rock, Paper and Scissor game")
    youwin,computerwin=0,0
    for i in range(1,6):##% round game
        print("Round",i,"Starts")
        print("Please select any option")
        print("1.Rock","2.Paper","3.scissor",sep="\n")##choices
        yourchoice=int(input())
        if yourchoice==1:
            print("You selected Rock " )
            yourchoice="Rock"
        elif yourchoice==2:
            print("You Selcted Paper")
            yourchoice="Paper"
        elif yourchoice==3:
            print("You selected Scissor")
            yourchoice="Scissor"
        else:
            print("invalid input!! please select a Valid input to countinue the game")
            break##if user inputs an invalid choice then the game will be stopped here
        computerchoice=random.choice(choice)##Computer will select here
        print("Computer select:",computerchoice)
    ##now we will see results
        if yourchoice==computerchoice:
            youwin+=1
            computerwin=+1
            print("This round is drawn")
        elif(yourchoice=="Paper" and computerchoice=="Rock") or (yourchoice=="Scissor" and computerchoice=="Paper") or (yourchoice=="Rock" and computerchoice=="Scissor"):
            youwin+=1
            print("You have win this round")
        else:
            computerwin+=1
            print("Computer has win this round")
    if youwin>computerwin:
        print("you win the game")
        print("score is:","your score: ",youwin,"computer score: ",computerwin,sep="")
    elif computerwin>youwin:
        print("Computer win the game")
        print("Score is:","computer score:",computerwin,"Your score: ",youwin,sep=" ")
    else:
        print("match is drawn")
        print("Score is: ","computer score: ",computerwin,"Your score: ",youwin,sep=" ")
    user_input=input("Do you want to play again?? (Yes/Exit)")
    if user_input=="Yes" or user_input=="yes" or user_input=="YES":
        continue
    else:
        break
