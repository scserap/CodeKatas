from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np


def prepare_paper(coordinates):
    max_x = np.max(coordinates[:,0]+1)
    max_y = np.max(coordinates[:, 1]+1)
    paper = np.zeros([max_y,max_x])
    for coordinate in coordinates:
        paper[coordinate[1],coordinate[0]] += 1
    return paper


def fold_paper(paper, instruction):
    instruction = instruction.split('=')
    if instruction[0] == 'x':
        folding_axis = 1
    else:
        folding_axis = 0
    folding_line = int(instruction[1])

    new_paper = np.split(paper, [folding_line], axis=folding_axis)
    new_paper2 = np.split(paper, [folding_line+1], axis=folding_axis)
    if folding_axis == 1 :
        new_paper = np.add(new_paper[0], np.fliplr(new_paper2[folding_axis]))
    else:
        new_paper = np.add(new_paper[0], np.flipud(new_paper2[1]))
    return new_paper


def main():
    print(datetime.now())
    dataset = read_file('real_dataset.txt')
    new_dataset = []
    instructions = []
    for row in dataset:
        row = row.replace('\n', '')
        if row[0:4]=='fold':
            instructions.append(row.replace('fold along ',''))
        else:
            if len(row)>0:
                new_dataset.append(row.split(','))

    coordinates = np.array(new_dataset,dtype=int)
    paper = prepare_paper(coordinates)
    print(np.count_nonzero(paper))
    x = 0
    for instruction in instructions:
        x += 1
        paper = fold_paper(paper,instruction)
    print(paper)
    print('Dot counts after {} instraction : {}, Debug to see the characters from paper array'.format(instruction,np.count_nonzero(paper)))

    # print(paper)
    # new_list, paths = find_paths(caves,caves, [])
    # print(np.array(paths))
    # print('total path count is {}'.format(len(paths)))
    # print(new_list)
    print(datetime.now())

if __name__ == "__main__":
    main()
