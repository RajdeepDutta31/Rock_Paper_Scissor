import random
ch_lst = ["rock", "paper", "scissor"]
def playgame():
    my_ch = input("Your turn: ").lower()
    if my_ch not in ch_lst:
        print("Invalid Choice")
        return -1
    
    com_ch = random.choice(ch_lst)
    print("Your choice is :",(my_ch.capitalize()))
    print("Computer's choice is :",(com_ch.capitalize()))
    
    if (my_ch=="rock" and com_ch =="scissor"):
        print("***You win***")
    elif (my_ch=="paper" and com_ch == "rock"):
        print("***You win***")
    elif (my_ch=="scissor" and com_ch == "paper"):
        print("***You win***")
    elif (my_ch==com_ch):
        print("***Draw***")
    else:
        print("***You lose***")

    ch = input("\nPress R to Replay ,Press any other key to Quit : ").upper()
    if ch=="R":
        replay()
    else:
        return -1
        
def replay():
    playgame()

playgame()

