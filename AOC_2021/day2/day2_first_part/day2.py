from AOC_2021.day1.day1 import read_file


def apply_command(command, unit:int, current_horizontal_position:int, current_depth:int):
    if command =='forward':
        current_horizontal_position += unit
    elif command =='down':
        current_depth += unit
    elif command =='up':
        current_depth -= unit
    return current_horizontal_position, current_depth


def move_submarine(commands):
    current_horizontal_position = 0
    current_depth = 0
    for command in commands:
        command, unit = command.split()
        current_horizontal_position, current_depth = apply_command(command,int(unit), current_horizontal_position, current_depth)
    return current_horizontal_position, current_depth


def main():
    commands = read_file('day2_input.txt')
    current_horizontal_position, current_depth = move_submarine(commands)
    print('current_horizontal_position = {}'.format(current_horizontal_position))
    print('current_depth = {}'.format(current_depth))
    print('Result of Multiply = {}'.format(current_depth*current_horizontal_position))


if __name__ == "__main__":
    main()
