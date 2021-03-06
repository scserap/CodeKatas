import numpy as np
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
        # print(board)
        for line in board:
            # print(line)
            sum_num = 0
            for num in line:
                # print('num={}'.format(num))
                sum_num += int(num)
                # print('sum_num={}'.format(sum_num))
                if num!='-1':
                    # print('num={}'.format(num))
                    break
                if sum_num==-5:
                    winning_board = board
                    break
            if winning_board:
                break
        if not winning_board:
            for i in range(0,5):
                sum_num = 0
                for k in range(0, 5):
                    sum_num += int(board[k][i])
                if sum_num == -5:
                    # print(board)
                    # print('sum_num == -5')
                    winning_board = board
                    break
        if winning_board:
            break
    return winning_board


def find_winning_board(draw_numbers_data, bingo_boards):
    draw_numbers = draw_numbers_data[0].split(',')
    winning_board = None
    winning_number = None
    for draw_number in draw_numbers:
        # print('draw_number={}'.format(draw_number))
        # print('bingo_boards={}'.format(bingo_boards))
        for board in bingo_boards:
            for line in board:
                for i in range(0,5):
                    # print('line[{}] = {}, draw_number = {}'.format(i,line[i],draw_number))
                    if line[i] == draw_number:
                        # print('line[i] == draw_number')
                        line[i] = '-1'
                        print(board)
        # print('bingo_boards in find={}'.format(bingo_boards))
        winning_board = find_if_there_is_winning_board(bingo_boards)
        print('winning_board in find={}, draw_number = {}'.format(winning_board,draw_number))
        while winning_board:
            last_winning_board = winning_board
            winning_number = draw_number
            if len(bingo_boards)==0:
                break
            else:
                bingo_boards.remove(winning_board)
                winning_board = find_if_there_is_winning_board(bingo_boards)
        if len(bingo_boards) == 0:
            break
    winning_board = last_winning_board
    return winning_board, int(winning_number)


def calculate_score(winning_board, winning_number):
    sum_board = 0
    for line in winning_board:
        if len(line)>0:
            for number in line:
                if number=='-1':
                    number=0
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
