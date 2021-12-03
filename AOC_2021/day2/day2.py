from AOC_2021.day1.day1 import read_file


def apply_command(command, unit:int, current_horizontal_position:int, current_depth:int, current_aim:int):
    if command =='forward':
        current_horizontal_position += unit
        current_depth = current_depth + (current_aim * unit)
    elif command =='down':
        current_aim += unit
    elif command =='up':
        current_aim -= unit
    return current_horizontal_position, current_depth, current_aim


def move_submarine(commands):
    current_horizontal_position = 0
    current_depth = 0
    current_aim = 0
    for command in commands:
        command, unit = command.split()
        current_horizontal_position, current_depth, current_aim = apply_command(command,int(unit), current_horizontal_position, current_depth, current_aim)
    return current_horizontal_position, current_depth


def main():
    commands = read_file('day2_input.txt')
    current_horizontal_position, current_depth = move_submarine(commands)
    print('current_horizontal_position = {}'.format(current_horizontal_position))
    print('current_depth = {}'.format(current_depth))
    print('Result of Multiply = {}'.format(current_depth*current_horizontal_position))


if __name__ == "__main__":
    main()
