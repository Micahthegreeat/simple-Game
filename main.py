#Miach Knox10/7/24
#a game about making products


import time
import random
import display
import parts
import sys
#defining starting variables
grid_size = 2
#dictionary with every board size
board = {}
for x in range(2,13):
    board[f"board{x}"] = [[['','',''] for j in range(x) ] for i in range(x)]
#dictionary with current machines avalible
machines = {
    'outlet' : {'name' : 'outlet', 'cost' : 50},
    'producer' : {'name' : 'producer', 'type' : 'iron'},
    'seller' : {'name' : 'seller', 'cost' : 25},
    'roller' : {'name' : 'roller', 'cost' : 25}

}
items = {
    'money' : 100
}

#example board for visualization
# [
# [['', '', ''], ['', '', '']],
# [['', '', ''], ['', '', '']]
# ]

# instructions for playing
def Readrules():
    print('''
The goal is to buy the 13 by 13 plot of factory
You start with a 2 by 2
You will build things by saying "build [level] [x cord] [y cord(measured from top to bottem)] [direction]"
You can sell things by saying "sell [x cord] [y cord(measured from top to bottem)] [direction]"
"direction" can be "up" "down" "left" "right"
"shop" for the shop
"items" to see what machines u have acess to
You can press enter instead of typing things to pass time
help will show what u can press
    ''')


def readOptions():
    print('''
build things by saying "build  [machine] [x cord] [y cord(measured from top to bottem)] [direction]"
sell things by saying "sell [x cord] [y cord(measured from top to bottem)] [direction]"
upgrade by saying "upgrade [x cord] [y cord(measured from top to bottem)] [direction]"
"direction" can be "up" "down" "left" "right"
"shop" for the shop
"items" to see what machines u have acess to
You can press enter instead of typing things to pass time
''')

def readMachines(machines):
    print('You have these machines avalible')
    for item in machines:
        print(item)
#to make the factory do stuff
def passtime():
    pass

#displays a shop
def shop():
    pass


def main():
    
    
    #starting the actual game loop

    running = True
    while running:
        start = input('Would you like to [r]ead the rules or [p]lay: ')
        while start != 'p' and start != 'r':
            start = input('Would you like to [r]ead the rules or [p]lay: ')
        if start == 'p':
            while True:
                if grid_size >= 13:
                    print('YOU WIN CONGRATS')
                    break
                display.board(board[f'board{grid_size}'])
                value = input('> ').strip().lower().split()
                if len(value) != 0:
                    if value[0] == 'help':
                        readOptions()
                    elif value[0] == 'shop':
                        pass
                    elif value[0] == 'build':
                        pass
                    elif value[0] == 'sell':
                        pass
                    elif value[0] == 'upgrade':
                        pass
                      
                    elif value[0] == 'items':
                        readMachines(machines)
                    else:
                        print('not an option') 
                else:
                    passtime()
        
        elif start == 'r':
            Readrules()
        

if __name__ == '__main__':
    main()