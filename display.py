def board(board):
    length = len(board)
    
    for row in board:
        print('|-------------' * length + '|')
        for i in range(3):
            for j in range(length):
                if i == 1:
                    print('|', end = '')
                    spaces = 13 - len(row[j][i]['name'])
                    print(' ' * (spaces//2) + row[j][i]['name'] + ' ' * (spaces//2) + ' ' * (spaces%2), end = '')
                else:
                    print('|', end = '')
                    spaces = 13 - len(row[j][i])
                    print(' ' * (spaces//2) + row[j][i] + ' ' * (spaces//2) + ' ' * (spaces%2), end = '')
            print('|')


    print('|-------------' * length + '|')

if __name__ == '__main__':
    board([
    [['', 'test', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', ''], ['', '', 'test'], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']],
    [['', '', ''], ['', '', ''], ['', '', ''], ['test', '', ''], ['', '', '']]
    ])