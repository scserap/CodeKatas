from AOC_2021.day1.day1 import read_file


def get_string_boards(bingo_board_lines):
    bingo_board_lines_string = ''
    new_line = ''
    for line in bingo_board_lines:
        new_line = line.replace("  ", " ").replace("\n", ";")
        bingo_board_lines_string += new_line
    return bingo_board_lines_string


def get_bingo_boards(bingo_board_lines):
    board = []
    boards = []
    bingo_board_lines.append('\n')
    for line in bingo_board_lines:
        new_line = line.replace(chr(10),"").replace("  ", " ").replace("\n", "")
        new_line_list = new_line.split(' ')
        for nline in new_line_list:
            if nline=='':
                new_line_list.remove(nline)
        if len(new_line_list)==0 :
            boards.append(board)
            board=[]
        else:
            board.append(new_line_list)

    return boards


def find_if_there_is_winning_board(boards):
    winning_board = None
    for board in boards:
        for line in board:
            print('len(line)={}'.format(len(line)))
            if len(line)==0:
                winning_board = board
        if winning_board:
            break
    return winning_board


def find_winning_board(draw_numbers_data, bingo_boards):
    draw_numbers = draw_numbers_data[0].split(',')
    winning_board = None
    winning_number = None
    for draw_number in draw_numbers:
        new_boards = []
        print('draw_number={}'.format(draw_number))
        print('bingo_boards={}'.format(bingo_boards))
        for board in bingo_boards:
            print('board={}'.format(board))
            new_board = [[ele for ele in sub if ele != draw_number] for sub in board]
            new_boards.append(new_board)
        bingo_boards = new_boards
        winning_board = find_if_there_is_winning_board(new_boards)
        print('winning_board in find={}'.format(winning_board))
        if winning_board:
            winning_number = draw_number
            print('break in find')
            break
    return winning_board,int(winning_number)


def calculate_score(winning_board, winning_number):
    sum_board = 0
    for line in winning_board:
        if len(line)>0:
            for number in line:
                sum_board += int(number)
    print('sum_board={}'.format(sum_board))
    score = sum_board * winning_number
    return score

def main():
    draw_numbers_data = read_file('day4_draw_numbers.txt')
    bingo_board_lines = read_file('day4_bingo_boards.txt')
    bingo_boards = get_bingo_boards(bingo_board_lines)
    winning_board, winning_number = find_winning_board(draw_numbers_data,bingo_boards)
    score = calculate_score(winning_board,winning_number)
    print('winning_board={}'.format(winning_board))
    print('winning_number={}'.format(winning_number))
    print('score={}'.format(score))

if __name__ == "__main__":
    main()
