import random
def main():
    print("Hello! Welcome to the rock paper sissors game!")
    print("The rule is as follows: two players secretly pick one of “rock,” “paper,” or “scissors.” Both players reveal their selection to the other player at once; the winner is chosen based on what the selections are. Rock beats scissors (by crushing them); scissors beats paper (by cutting it); and paper beats rock (by covering it). If both players select the same one, it is a tie.")
    print("Please enter your choice! Your choice could be rock, paper, or sissors: ")
    x = input()
    y = random.choice(["rock", "paper", "scissors"])
    win = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
    loss = {"rock":"paper", "paper":"scissors", "scissors":"rock"}
    tie = {"rock":"rock", "paper":"paper", "scissors":"scissors"}
    result = "You selected " + x + " and the computer selected " + y + ". ";
    if win[x] == y:
        result += "The winner is you!"
    elif loss[x] == y:
        result += "The winner is the computer!"
    elif tie[x] == y:
        result += "The game reached a tie!"
    else:
        result += "Illegal choice entered!"
    print(result)
    

if __name__ == "__main__":
    main()
