import random



moves=("rock","paper","scissor")
keep_playing = "true"
print("Lets Play a Game","\U00002B07")




while keep_playing=="true":
    smove=random.choice(moves)

    pmove=input("What's your move ( rock , paper, scissor )?")
    print("The computer choice is", smove,".")


    if smove==pmove:
        print("The Game is Tie","\U0001f44e")
    elif pmove =="rock" and smove == "paper":
        print("System Wins","\U0001f44e")
    elif pmove =="rock" and smove == "scissor":
        print("You Wins","\U0001f497")
    elif pmove =="paper" and smove == "rock":
        print("You Wins","\U0001f497")
    elif pmove =="paper" and smove == "scissor":
        print("System Wins","\U0001f44e")
    elif pmove =="scissor" and smove == "rock":
        print("System Wins","\U0001f44e")
    elif pmove =="scissor" and smove == "paper":
        print("You Wins","\U0001f497")


