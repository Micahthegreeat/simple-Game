def board(grid_size, board):
    length = len(board)
    
    for row in board:
        print('|-------------' * length + '|')
        print('|             ' * length + '|')
        for word in row:
            print('|', end = '')
            spaces = 13 - len(word)
            print(' ' * (spaces//2) + word + ' ' * (spaces//2) + ' ' * (spaces%2), end = '')

        print('|')
        print('|             ' * length + '|')
    print('|-------------' * length + '|')

if __name__ == '__main__':
    board(5, [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']])