"""
TIC TAC TOE program by SnowKit08
"""

def header():
    print("\n -----------------------------")
    print("|*** LET'S PLAY TICTACTOE! ***|")
    print(" -----------------------------\n")


def scoreboard(player1, player2, p1_score, p2_score):
    print("==========SCOREBOARD==========")
    print(player1 + "       ", p1_score)
    print(player2 + "       ", p2_score)
    print("-" * 30)
    if p1_score > p2_score:
        print("The current winner is " + player1, "\n")
    elif p2_score > p1_score:
        print("The current winner is " + player2, "\n")
    else:
        print(player1 + " and " + player2 + " are currently tied!\n")


def show_options():
    user_option = input("CHOOSE AN OPTION:\n1:play new game\n2:change player names\n3:exit program\n")
    while user_option not in ["1", "2", "3"]:
        user_option = input("Invalid user option. Try Again\n")
    return int(user_option)


def show_help():
    print("\n========HOW TO PLAY========")
    print("Every place on the board has a specified position as follows:")
    print_board([x for x in range(1, 10)])
    print("When it is your turn enter the corresponding number to take that position ")
    print("Players take turns starting new games.\n")
    input("Press Enter to continue . . .")


def congrats(winner):
    print("*" * (26 + len(winner)))
    print("CONGRADULATIONS " + winner + "! YOU WON!")
    print("*" * (26 + len(winner)))
    input("\nPress Enter to continue . . .")


def print_board(values):
    hori_row = " _______|_______|_______ "
    vert_row = "        |       |"
    print(vert_row)
    print("    {}   |   {}   |   {}".format(values[0], values[1], values[2]))
    print(hori_row)
    print(vert_row)
    print("    {}   |   {}   |   {}".format(values[3], values[4], values[5]))
    print(hori_row)
    print(vert_row)
    print("    {}   |   {}   |   {}".format(values[6], values[7], values[8]))
    print(vert_row, "\n")


def check_win(taken_positions):
    win_sol = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_combo in win_sol:
        if all(item in taken_positions for item in win_combo)is True:
            return True
    return False


def play_game(starting_player, player1, player2):
    #SETUP FOR THE ROUND
    header()
    values = [" "] * 9
    X_positions = []
    O_positions = []
    game_on = True
    #ESTABLISH X & O ASSIGNMENT BY STARTING_PLAYER
    if starting_player == 1:
        players_icons = [player1,player2,"X","O"]
    else:
        players_icons = [player2,player1,"X","O"]
    first_player_icon = input("\nPlayer: "+players_icons[0]+", please choose to be X's or O's:\n")
    while first_player_icon not in ["O","X","o","x","0"]:
        first_player_icon = input("Invalid option. Pls try again.\nPlease select to play either X's or O's:")
    if first_player_icon != "X" and first_player_icon !="x":
        players_icons[2]="O"
        players_icons[3]="X"
    cur_player = players_icons[0]
    cur_player_icon = players_icons[2]
    print_board(values)
    #THE LOOP THAT EXECUTES EACH MOVE
    while game_on is True:
        #CHECKS VALID POSITION
        try:
            position = int(input("It is "+cur_player+"'s turn. Enter the position for "+cur_player_icon+":"))
        except ValueError:
            print("Invalid position: Not a digit. Please try again.\n")
            continue
        if int(position) > 9 or int(position) < 1:
            print("Invalid position: Out of range. Please try again.\n")
            continue
        if values[int(position)-1] != " ":
            print("Invalid position: Space already taken. Please try again.\n")
            continue 
        #PUTS ICON IN BOARD + RECORDS X OR O'S MOVE
        values[int(position)-1] = cur_player_icon
        if cur_player_icon == "O":
            O_positions.append(int(position))
        else:
            X_positions.append(int(position))
        print_board(values)
        #CHECKS CURRENT PLAYER TURNS IF THEY WON. IF SO, RETURN WINNER
        if len(X_positions) >= 3 or len(O_positions) >= 3:
            if cur_player_icon == "O":  
                if check_win(O_positions)== True:
                    return cur_player
            else:
                if check_win(X_positions)== True:
                    return cur_player
        #DECLARE A TIE IF BOARD IS COMPLETELY FILLED. 
        if " " not in values:
            print("------------------------------------------------------")
            print("GAME OVER! All positions are full, it ended in a tie. ")
            print("------------------------------------------------------")
            input("\nPress Enter to continue . . .")
            return None
            
        #SWITCHES THE CURRENT PLAYER
        if players_icons.index(cur_player)%2 == 0:
            cur_player = players_icons[1]
            cur_player_icon = players_icons[3]
        else:
            cur_player = players_icons[0]
            cur_player_icon = players_icons[2]
    

def change_player_name(old_nameP1, old_nameP2):
    #RETURNS PLAYER TO BE CHANGED + THE NEW NAME
    player_change = input("Which players name do you want to change?\nEnter a 1 or 2. Or to exit enter 3\n")
    while player_change not in ["1","2","3"]:
        player_change = input("Invalid option.\nPlease try again: ")
    if player_change == "3":
        return 0, None
    else:
        if player_change == "1":
            old_name = old_nameP1
        else:
            old_name = old_nameP2
        new_name = input("Enter " + old_name + "'s New Name: ")
        input("\nPlayer "+player_change+"'s name has been changed to "+new_name+". Press Enter to continue.\n")
        return int(player_change), new_name
    

def main():
    #STARTING SCREEN + INSTRUCTIONS
    header()
    player1 = input("Enter Player 1 Name: ")
    player2 = input("Enter Player 2 Name: ")
    starting_player = 1
    p1_score = 0
    p2_score = 0
    show_help()
    game_status = True
    #MAIN MENU
    while game_status is True:
        header()
        scoreboard(player1, player2, p1_score, p2_score)
        user_option = show_options()
        #PLAY GAME OPTION
        if user_option == 1:  
            result = play_game(starting_player, player1, player2)
            if result != None:
                if result == player1:
                    congrats(player1)
                    p1_score += 1
                else:
                    congrats(player2)
                    p2_score += 1
            if starting_player == 1:
                starting_player = 2
            else:
                starting_player = 1
        #CHANGE PLAYER'S NAMES OPTION
        elif user_option == 2:
            option,new_name = change_player_name(player1,player2)
            if option == 0:
                continue
            else:
                if option == 1:
                    player1 = new_name
                else:
                    player2 = new_name
        #QUITS THE PROGRAM OPTION
        else:
            quit_game = input("\nYou are about to quit the program. Are you sure? (y/n)\n")
            if quit_game == 'y':
                game_status = False
            else:
                continue
    #ENDING SCREEN
    if p1_score > p2_score:
        print(player1 + " wins with a final score of", p1_score, ":", p2_score)
    elif p2_score > p1_score:
        print(player2 + " wins with a final score of", p2_score, ":", p1_score)
    else:
        print("It ended in a tie!", "Final score is {0}:{0}".format(p1_score))
    print("THANK YOU BOTH FOR PLAYING!!!")


main()
