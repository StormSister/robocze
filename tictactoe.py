import os
# drukuje plansze
def print_board(values):
  print("   1   2   3")
  print(f"A  {values[0]} | {values[1]} | {values[2]}")
  print("   ---+---+---")
  print(f"B  {values[3]} | {values[4]} | {values[5]}")
  print("   ---+---+---")
  print(f"C  {values[6]} | {values[7]} | {values[8]}")


# drukuje tablice wynikow
def print_scoreboard(score_board):
    print("\t--------------------------------")
    print("\t              SCOREBOARD       ")
    print("\t--------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t--------------------------------\n")


# sprawdza czy ktokolwiek wygral
def check_win(player_pos, cur_player):
    # wszystkie warunki wygranej
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # czy sa spelnine warunki wygranej
    for x in soln:
        if all(y in player_pos[cur_player] for y in x):

            return True

    return False


# czy jest remis
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


def translate_input(input):
  if input == 'A1':
    return int(1)
  elif input == 'A2':
    return int(2)
  elif input == 'A3':
    return int(3)
  elif input == 'B1':
    return int(4)
  elif input == 'B2':
    return int(5)
  elif input == 'B3':
    return int(6)
  elif input == 'C1':
    return int(7)
  elif input == 'C2':
    return int(8)
  elif input == 'C3':
    return int(9)



def single_game(cur_player):
    # pola startowe z '.'
    values = ['.' for x in range(9)]

    # zachowuje zajete pozycje
    player_pos = {'X': [], 'O': []}

    # pojedyncza gra
    while True:
        print_board(values)
       

        print(f"Player {cur_player}\nWhere do you want to put the {cur_player}?\nFirst digit : A,B or C specify the column\nSecond digit also 1,2,3 specify the row\n",
                end="")
        input_values = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        player_input = input().upper()
        if player_input in input_values:
            print(player_input)
        else:
            print("Wrong Input!!! Try Again")
            continue
        
        move = translate_input(player_input)
        

        # Czy pole jest zajete
        if values[move - 1] != '.':
            
            print("Place already filled. Try again!!")
            
            continue

        # informacje do tablicy wynikow

        # stan tablicy
        values[move - 1] = cur_player
        os.system('cls')

        # pozycja gracza
        player_pos[cur_player].append(move)

        # kto wygral
        if check_win(player_pos, cur_player):
            print_board(values)
            print("Player ", cur_player, " has won the game!!")
            print("\n")
            return cur_player
        #czy jest remis
        if check_draw(player_pos):
            print_board(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # zmiana graczy
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


if __name__ == "__main__":

    print("Player 1")
    player1 = input("Enter the name : ")
    print("\n")

    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")

    # kto wybral kolko a kto krzyzyk
    cur_player = player1

    # zachowuje wybory graczy
    player_choice = {'X': "", 'O': ""}

    # O czy X
    options = ['X', 'O']

    # tablica wynikow
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    # p
    while True:

        # wybor menu
        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")


        try:
            choice = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again\n")
            continue


        if choice == 1:
            player_choice['X'] = cur_player
            if cur_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1

        elif choice == 2:
            player_choice['O'] = cur_player
            if cur_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1

        elif choice == 3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wrong Choice!!!! Try Again\n")

        #zwyciezca gry pojedynczej
        winner = single_game(options[choice - 1])

        # wpisuje zwyciezc do tablicy wynikow
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1

        print_scoreboard(score_board)
        # zmienia gracza ktory wybral O lub X
        if cur_player == player1:
            cur_player = player2
        else:
            cur_player = player1