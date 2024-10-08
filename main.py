#Miach Knox10/7/24
#a game about making products


import time
import random
import display
import parts
import sys

#dictionary with every board size
defaultPiece = ['', {'name': ''}, '', '']
board = {}
for x in range(2,13):
    board[f"board{x}"] = [[defaultPiece for j in range(x) ] for i in range(x)]
#dictionary with mahines 


    


#example board for visualization
# [
# [['', {'name': ''}, '', ''], ['', {'name': ''}, '', '']],
# [['', {'name': ''}, '', ''], ['', {'name': ''}, '', '']]
# ]

# instructions for playing
def Readrules():
    print('''
The goal is to buy the 13 by 13 plot of factory
You start with a 2 by 2
You will build things by saying "build [x cord] [y cord(measured from top to bottem)] [direction]"
if ther is no direction skip that
You can sell things by saying "sell [x cord] [y cord(measured from top to bottem)]"
"direction" can be "up" "left" "right" (notice how there is no down)
"shop" for the shop
"items" to see what machines u have acess to
You can press enter instead of typing things to pass time
help will show what u can press
you type quit to leave
clear to start the board over
''')


def readOptions():
    print('''
You will build things by saying "build [x cord] [y cord(measured from top to bottem)] [direction] "
if there is no direction skip that
sell things by saying "sell [x cord] [y cord(measured from top to bottem)]"
upgrade by saying "upgrade [x cord] [y cord(measured from top to bottem)]"
"direction" can be "up" "left" "right" (notice how there is no down)
"shop" for the shop
"items" to see what machines u have acess to
You can press enter instead of typing things to pass time
you type quit to leave
clear to start the board over
help [machine] will tell u what it does
buy will buy the next level
''')

def readMachines(machines):
    print('You have these machines avalible')
    for item in machines:
        print(item)


#displays a shop
def shop(machines, money):
    print('These are what you can buy:')
    list = []
    for item in parts.machine():
        if not(item in machines):
            print(item, end = '')
            print('        cost:', parts.part(item)['cost'])
            list.append(item)
    print('\nYou can [l]eave the shop, [b]uy the machine, or [a]sk what the machine does')
    while True:
        key = input('> ').strip().lower().split()
        if len(key) == 0: continue
        if key[0] == 'l':
            return machines, money
            break
        elif key[0] == 'a':
            a = input('what machine? ')
            parts.machinedescription(a)
        elif key[0] == 'b':
            a = input('what machine? ')
            if a in list and parts.part(a)['cost'] < money:
                machines[a] = parts.part(a)
                money -= parts.part(a)['cost']
                print(f'you have {money} money left')
            else:print('not an option')
        elif len(key[0]) > 1:
            print('you are still in the shop')
            print('You can [l]eave the shop, [b]uy the machine, or [a]sk what the machine does')

def check():
    for item in parts.machine():
        if len(item) > 12:
            print(item, 'is to long of a name fix it')
            sys.exit    

#clears the board and reinburses the player the money they spent
def clear(board, money):
    for j, i in enumerate(board):
        for k, machine in enumerate(i):
            if 'cost' in machine[1]:
                money += machine[1]['cost']
            board[j][k] = defaultPiece
    return money, board


def main():
    # checks that all hardcoded values are ok inputs
    check()
    
    
    #starting the actual game loop

    running = True
    while running:
        start = input('Would you like to [r]ead the rules or [p]lay: ')
        while start != 'p' and start != 'r':
            start = input('Would you like to [r]ead the rules or [p]lay: ')
        if start == 'r':
            Readrules()
            start = 'p'
        if start == 'p':
            #defining starting variables
            grid_size = 2
            money = 125
            machines = {
                'outlet' : parts.part('outlet'),
                'producer' : parts.part('producer'),
                'seller' : parts.part('seller'),
                'roller' : parts.part('roller')

            }
            while True:
                if grid_size >= 13:
                    print('YOU WIN CONGRATS')
                    break
                display.board(board[f'board{grid_size}'])
                print('Money:', money)
                value = input('> ').strip().lower().split()
                if len(value) != 0:
                    if value[0] == 'help' and len(value) == 0: 
                        readOptions()
                    elif value[0] == 'help':
                        parts.machinedescription(value[1])
                    elif value[0] == 'shop' or value[0] == 'store':
                        machines, money = shop(machines, money)
                    elif value[0] == 'build':
                        pass
                    elif value[0] == 'clear':
                        money, board[f'board{grid_size}'] = clear(board[f'board{grid_size}'], money)
                    elif value[0] == 'quit':
                        sys.exit()
                    elif value[0] == 'sell':
                        pass
                    elif value[0] == 'upgrade':
                        pass
                    elif value[0] == 'buy':
                        pass
                    elif value[0] == 'items':
                        readMachines(machines)
                    else:
                        print('not an option') 
                else:
                    board[f'board{grid_size}'], money = parts.time(board[f'board{grid_size}'], money)
        
        
        

if __name__ == '__main__':
    main()