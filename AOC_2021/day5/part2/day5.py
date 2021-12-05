
from AOC_2021.day1.day1 import read_file
import numpy as np


def convert_dataset(dataset):
    np_dataset = np.array(dataset,int)
    vertical = np_dataset[np.where(np_dataset[:,0]== np_dataset[:,2])]
    horizontal = np_dataset[np.where(np_dataset[:, 1] == np_dataset[:, 3])]
    diagonal = np_dataset[np.where(abs(np_dataset[:,0]-np_dataset[:,2])==abs(np_dataset[:,1]-np_dataset[:,3]) )]
    # print('vertical={}'.format(vertical))
    # print('horizontal={}'.format(horizontal))
    # print('diagonal={}'.format(diagonal))
    matrix_size = np.max(np_dataset)+1
    diagram = np.zeros((matrix_size,matrix_size), dtype=int)
    for line in vertical:
        print('line={}'.format(line))
        max_y = line[1] if line[1] > line[3] else line[3]
        min_y = line[3] if line[1] > line[3] else line[1]
        for i in range(min_y, max_y+1):
            # print('i={},line[1]={},line[3]={},line[0]={},min_y={},max_y={}'.format(i,line[1],line[3],line[0],min_y,max_y))
            diagram[i,line[0]] += 1
            # print(diagram)

    for line in horizontal:
        print('line={}'.format(line))
        max_x =line[0] if line[0] > line[2] else line[2]
        min_x = line[2] if line[0] > line[2] else line[0]
        for i in range(min_x,max_x+1):
            # print('i={},line[0]={},line[2]={},line[1]={},min_x={},max_x={}'.format(i,line[0],line[2],line[1],min_x,max_x))
            diagram[line[1],i] += 1

    for line in diagonal:
        print('line={}'.format(line))
        points = abs(line[0]-line[2])
        start_x = line[2] if line[0]>line[2] else line[0]
        start_y = line[3] if line[0]>line[2] else line[1]
        end_y = line[1] if line[0]>line[2] else line[3]
        sign_y = +1 if end_y > start_y else -1
        for i in range(0, points + 1):
            # print('i={},start_x+i={},start_y + sign_y*i={},points={}, end_y={}, sign_y={}'.format(i,start_x+i,start_y + sign_y*i,points,end_y,sign_y))
            diagram[start_y + sign_y*i,start_x+i] += 1
    print(diagram)
    return len(np.where(diagram[:, ] >= 2)[0])


def main():
    # [None if x == ' -> ' else x.replace(' -> ',',').replace('\n', '') for x in dataset]
    dataset = read_file('day5_dataset.txt')
    new_dataset = [x.replace(' -> ', ',').replace('\n', '').split(',') for x in dataset]
    two_or_more_points = convert_dataset(new_dataset)
    print(two_or_more_points)


if __name__ == "__main__":
    main()
