import os

a = ":  "
b = "  :"
line1 = "..................."
line2 = ":     :     :     :"
out = [1, 2, 3, 4, 5, 6, 7, 8, 9]
p1win = False
p2win = False
player1 = 1
player2 = 2
winner = False


def clear():
    os.system('cls')


def print_box(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    def box(num1=" ", num2=" ", num3=" "):
        def box1(num1):
            print(a, end="")
            print(num1, end="")
            print(b, end="")
      
        def box2(num2):
            print(" ", num2, end="")
            print(b, end="")
        
        def box3(num3):
            print(" ", num3, end="")
            print(b)
        box1(num1)
        box2(num2)
        box3(num3)
        
    print(line1)
    print(line2)
    box(p1, p2, p3)
    print(line2)
    print(line1)
    print(line2)
    box(p4, p5, p6)
    print(line2)
    print(line1)
    print(line2)
    box(p7, p8, p9)
    print(line2)
    print(line1)


def initialize_input():
    global player1
    global player2
    while player1 not in ['x', 'X', 'o', 'O']:
        player1 = input("Player1, you want to be an X or O? ")
        if player1 not in ['x', 'X', 'o', 'O']:
            continue
        player1 = player1.upper()
        if player1 == "X":
            player2 = "O"
        else:
            player2 = "X"
        print(f"Player1 is {player1} and player2 is {player2}")


def initialize_variables():
    global out
    global p1win
    global p2win
    global winner
    out = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p1win = False
    p2win = False
    winner = False


def take_input(player):
    position = "one"
    print(f"{player}, enter the position you want to change")
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        position = input("Please enter in range(1-9)")
        if position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            continue
        elif position in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = int(position)
    if position in range(1, 10):
        if out[position-1] not in ["X", "O"]:
            out[position-1] = player
            clear()
            print_box(*out)
        elif out[position-1] in ['X', 'O']:
            print("That position is already taken")
            take_input(player)


def win_check():
    
    def print_winner(n):
        global p1win
        global p2win
        if out[n] == player1:
            p1win = True
        elif out[n] == player2:
            p2win = True
    
    if out[0] == out[1] == out[2]:
        print_winner(0)
    if out[3] == out[4] == out[5]:
        print_winner(3)
    if out[6] == out[7] == out[8]:
        print_winner(6)
    if out[0] == out[3] == out[6]:
        print_winner(0)
    if out[1] == out[4] == out[7]:
        print_winner(1)
    if out[2] == out[5] == out[8]:
        print_winner(2)
    if out[0] == out[4] == out[8]:
        print_winner(0)
    if out[2] == out[4] == out[6]:
        print_winner(2)

    def final():
            if p1win == True and p2win == True:
                print("Congratulations, Both Player1 and Player2 won... it's a draw")
            elif p1win == True:
                print("Congratulations Player1 is the winner...")
            elif p2win == True:
                print("Congratulations Player2 is the winner...")            
    final()
    def judge():
        if p1win == True or p2win == True:
            return True
        else:
            return False
    looping = judge()
    return looping


def play_again():
    global winner
    again = 0
    while again not in ['y', 'Y', 'n', 'N']:
        again = input("Do you want to play again(Y/N): ")
    again = again.upper()
    if again == 'Y':
        start_the_game()
    elif again == 'N':
        winner = False


def start_the_game():
    global winner
    initialize_input()
    initialize_variables()
    clear()
    print_box(*out)
    lose = 0
    winner = win_check()
    while winner == False:
        if lose == 4:
            print("Both Player1 and Player2 didn't win...")
            play_again()
            break
        take_input(player1)
        take_input(player2)
        winner = win_check()
        lose += 1


start_the_game()
while winner == True:
    play_again()
