import random

comp_score = 0
player_score = 0
n_round=[]


def Choose_Option():
    user_choice = input("Choose s for Stone, p for Paper or s for Scissors(s): ")
    if user_choice in ["r","R"]:
        user_choice = "r"
    elif user_choice in [ "p", "P"]:
        user_choice = "p"
    elif user_choice in [ "s", "S"]:
        user_choice = "s"
    else:
        print("Option not recognized, enter your choice again .")
        Choose_Option()
    return user_choice


def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")

    user_choice = Choose_Option()
    comp_choice = Computer_Option()

    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("Player chose rock. The computer chose rock. Player tied.")

        elif comp_choice == "p":
            print("Player chose rock. The computer chose paper. Player lose.")
            comp_score += 1

        elif comp_choice == "s":
            print("Player chose rock. The computer chose scissors. Player win.")
            player_score += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("Player chose paper. The computer chose rock. Player win.")
            player_score += 1

        elif comp_choice == "p":
            print("Player chose paper. The computer chose paper. Player tied.")


        elif comp_choice == "s":
            print("Player chose paper. The computer chose scissors. Player lose.")
            comp_score += 1

    elif user_choice == "s":
        if comp_score == "r":
            print("Player chose scissors. The computer chose rock. Player lose.")
            comp_wins += 1

        elif comp_choice == "p":
            print("Player chose scissors. The computer chose paper. Player win.")
            player_score += 1

        elif comp_choice == "s":
            print("Player chose scissors. The computer chose scissors. Player tied.")

    print("")
    print("Player Score: " + str(player_score))
    print("Computer Score: " + str(comp_score))
    print("")


    if player_score + comp_score < 3:
        pass
    elif player_score + comp_score ==3:
        if player_score > comp_score:
            print("Congratulation player won the match")
        elif comp_score > player_score:
            print("try again, computer won the match")
        print("Game Over")
        break
    else:
        break