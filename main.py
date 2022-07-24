# mini rock paper scissors game
import random
import time

print("\n== Mini Rock Paper Scissors Game ==")
print("[ Rock = r, Paper = p, Scissors = s ]")
print("1. Start the game")
print("E. Exit the game")
choice = input("choice: ")

game_list = ["Rock", "Paper", "Scissors"]
game_point = 3
game_score = 0
user_choice = ""
user_score = 0
comp_turn = ""
comp_choice = ""
comp_score = 0

print("\n== Start Game ==")
if choice == '1':
    while True:                                                # loop again if user wants to keep playing
        game_score = 0                                         # reset point
        while game_score != game_point:
            user_turn = input("\nYour turn: ")
            if user_turn == 'r':
                user_choice = "Rock"
                comp_choice = random.choice(game_list)         # computer generate random choice from game_list
                if comp_choice == "Rock":                      # match randome generated choice to specific name to compare later
                    comp_turn = 'r'
                elif comp_choice == "Paper":
                    comp_turn = "p"
                elif comp_choice == "Scissors":
                    comp_turn = "s"
                for i in range(1, 0, -1):                     # give flow to the game, pause for several seconds before continue
                    print('---', end="")
                    time.sleep(1)  # give little flow in the game
                print("\nComputer's turn: ", comp_turn)
                if user_choice == "Rock" and comp_choice == "Rock":
                    print("\n> Tie")
                    print("Your score:", user_score)
                    print("Computer's score: ", comp_score)
                elif user_choice == "Rock" and comp_choice == "Paper":
                    print("\n> Computer got the point!")
                    comp_score += 1
                    print("Your score:", user_score)
                    print("Computer's score: ", comp_score)
                elif user_choice == "Rock" and comp_choice == "Scissors":
                    print("\n> You got the point!")
                    user_score += 1
                    print("Your score:", user_score)
                    print("Computer's score: ", comp_score)

            elif user_turn == 'p':
                user_choice = "Paper"
                comp_choice = random.choice(game_list)
                if comp_choice == "Rock":
                    comp_turn = 'r'
                elif comp_choice == "Paper":
                    comp_turn = "p"
                elif comp_choice == "Scissors":
                    comp_turn = "s"
                for i in range(1, 0, -1):
                    print('---', end="")
                    time.sleep(1)  # give little flow in the game
                print("\nComputer's turn: ", comp_turn)
                if user_choice == "Paper" and comp_choice == "Paper":
                    print("\n> Tie")
                    print("Your score:", user_score)
                    print("Computer's score: ", comp_score)
                elif user_choice == "Paper" and comp_choice == "Rock":
                    print("\n> You got the point!")
                    user_score += 1
                    print("Your score:", user_score)
                    print("Computer's score: ", comp_score)
                elif user_choice == "Paper" and comp_choice == "Scissors":
                    print("\n> Computer got the point!")
                    comp_score += 1
                    print("Your score:", user_score)
                    print("Computer's score: ", comp_score)

            elif user_turn == 's':
                user_choice = "Scissors"
                comp_choice = random.choice(game_list)
                if comp_choice == "Rock":
                    comp_turn = 'r'
                elif comp_choice == "Paper":
                    comp_turn = "p"
                elif comp_choice == "Scissors":
                    comp_turn = "s"
                for i in range(1, 0, -1):
                    print('---', end="")
                    time.sleep(1)  # give little flow in the game
                print("\nComputer's turn: ", comp_turn)
                if user_choice == "Scissors" and comp_choice == "Scissors":
                    print("\n> Tie")
                    print("Your score:", user_score)
                    print("Computer's score: ", comp_score)
                elif user_choice == "Scissors" and comp_choice == "Rock":
                    print("\n> Computer got the point!")
                    comp_score += 1
                    print("Your score:", user_score)
                    print("Computer's score: ", comp_score)
                elif user_choice == "Scissors" and comp_choice == "Paper":
                    print("\n> You got the point!")
                    user_score += 1
                    print("Your score:", user_score)
                    print("Computer's score: ", comp_score)
            else:
                print("\n[ Invalid input ]")

            if user_score > comp_score:
                game_score = user_score
            else:
                game_score = comp_score
                
        play_again = input("\nWould you like to play again (y/n)?")   # ask if user wants to play again
        if play_again == "n" or play_again == 'N':
            break


elif choice == 'e' or choice == 'E':
    print("\n--  Exit Game --")
else:
    print("\n[ Invalid choice ]")


if user_score == game_point:
    print("\n========================\n\nCongratulations! You won the game!")
elif comp_score == game_point:
    print("\n====================\n\nHa ha ha ... You lose!\nThis is a good opportunity for us to take over humanity!")

print("\n==  End Game  ==")
