import random

hi = 'hello'

print(hi);

print(len(hi))

print(hi.upper())

print(hi[2])

# random = a library - randint = function in random
print(random.randint(1, 10))

favourite_drink = 'coffee'

# making strings in python
print('My Favourite drink is ' + favourite_drink)
# OR
print('My favourite drink is {}'.format(favourite_drink))

input_one = ["  ", "1", "  |   ", "2", "   |   ", "3", "  "]
input_two = ["  ", "4", "  |   ", "5", "   |   ", "6", "  "]
input_three = ["  ", "7", "  |   ", "8", "   |   ", "9", "  "]

def print_input(input_array):
    line = ""
    for i in input_array:
        line +=i
    print line


vert = "     |       |       "
hor = "--------------------"

def board():
    print(vert)
    print_input(input_one)
    print(vert)
    print(hor)
    print(vert)
    print_input(input_two)
    print(vert)
    print(hor)
    print(vert)
    print_input(input_three)
    print(vert)


board()

class Player:
  def __init__(self, name, piece):
    self.name = name
    self.piece = piece

player_one = Player('Player 1', 'X')
player_two = Player('Player 2', 'O')

players = [player_one, player_two]
print(players[0].piece)
print(input_one[1])

def numCheck(num):
    if num == 1 and input_one[1] != players[0].piece and input_one[1] != players[1].piece:
        input_one[1] = players[0].piece 
    elif num == 2 and input_one[3] != players[0].piece and input_one[3] != players[1].piece:
        input_one[3] = players[0].piece 
    elif num == 3 and input_one[5] != players[0].piece and input_one[5] != players[1].piece:
        input_one[5] = players[0].piece 
    elif num == 4 and input_two[1] != players[0].piece and input_two[1] != players[1].piece:
        input_two[1] = players[0].piece 
    elif num == 5 and input_two[3] != players[0].piece and input_two[3] != players[1].piece:
        input_two[3] = players[0].piece 
    elif num == 6 and input_two[5] != players[0].piece and input_two[5] != players[1].piece:
        input_two[5] = players[0].piece 
    elif num == 7 and input_three[1] != players[0].piece and input_three[1] != players[1].piece:
        input_three[1] = players[0].piece 
    elif num == 8 and input_three[3] != players[0].piece and input_three[3] != players[1].piece:
        input_three[3] = players[0].piece
    elif num == 9 and input_three[5] != players[0].piece and input_three[5] != players[1].piece:
        input_three[5] = players[0].piece
    else:
        print("Please select a valid number")
        num = int(input())
        numCheck(num)

def winCheck():
    if (input_one[1] == input_one[3] == input_one[5]) or (input_two[1] == input_two[3] == input_two[5]) or (input_three[1] == input_three[3] == input_three[5]) or (input_one[1] == input_two[1] == input_three[1]) or (input_one[3] == input_two[3] == input_three[3]) or (input_one[5] == input_two[5] == input_three[5]) or (input_one[1] == input_two[3] == input_three[5]) or (input_one[5] == input_two[3] == input_three[3]):
        return True

def switchPlayers():
    temp = players[1]
    players[1] = players[0]
    players[0] = temp


def play():
    g_over = False
    count = 0
    while(g_over == False):
        board()
        print('{} please type the number of where you would like to place your piece.'.format(players[0].name))
        num = int(input())
        numCheck(num)
        switchPlayers()
        count +=1
        if count == 9 
            board()
            g_over = True
            print('We have a Winner! {}, well done!'.format(players[1].name) )
        elif winCheck():
            board()
            g_over = True
            print('It`s a draw!' )
  

play()

