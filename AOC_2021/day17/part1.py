from datetime import datetime
import numpy as np


def step_pos(pos,velocity):
    pos[0] += velocity[0]
    pos[1] += velocity[1]
    return pos


def step_velocity(velocity):
    if velocity[0]>0:
        velocity[0] -=1
    elif velocity[0]<0:
        velocity[0] += 1
    velocity[1] -= 1
    return velocity


def step(pos,velocity):
    pos = step_pos(pos,velocity)
    velocity = step_velocity(velocity)
    return pos, velocity


def find_velocities():
    velocities = []
    paths = []
    for x in range(-min_pos[0]*3,max_pos[0]*3):
        for y in range(min_pos[1]*3,abs(max_pos[1])*3):
            start_velocity = [x,y]
            velocity = [x,y]
            pos = [0, 0]
            path =[]
            print('Start velocity={}'.format(velocity))
            while pos[0] not in range(min_pos[0],max_pos[0]+1) or pos[1] not in range(min_pos[1],max_pos[1]+1):
                pos, velocity = step(pos,velocity)
                path.append([pos[0],pos[1]])
                if pos[0] in range(min_pos[0], max_pos[0]+1) and pos[1] in range(max_pos[1],min_pos[1]+1):
                    velocities.append(start_velocity)
                    paths.append(path)
                    print('{}. Final pos={}'.format(len(paths),pos))
                    print('{}. Final velocity={}'.format(len(paths),velocity))
                    break
                if (pos[0] > min_pos[0]+1 and pos[0] > max_pos[0]+1 ) or (pos[1] < min_pos[1]+1 and pos[1] < max_pos[1]+1):
                    break

    max_y = 0
    for path in paths:
        for pos in path:
            if pos[1]>max_y:
                max_y=pos[1]

    velocities = np.array(velocities)
    velocities = np.unique(velocities,axis=0)
    # print('Max y={}, velocity count= {}'.format(max_y,len(velocities)))
    return velocities,max_y


def main():
    print(datetime.now())
    with open('real_dataset.txt') as f:
        dataset = f.read().replace('target area: ','').split(', ')
    x = dataset[0].replace('x=','').split('..')
    y = dataset[1].replace('y=', '').split('..')
    global min_pos, max_pos
    min_pos = [int(x[0]),int(y[1])]
    max_pos = [int(x[1]),int(y[0])]
    print('min_pos={}'.format(min_pos))
    print('max_pos={}'.format(max_pos))
    velocities,max_y = find_velocities()
    print('Max y={}, velocity count= {}'.format(max_y, len(velocities)))
    print(datetime.now())

if __name__ == "__main__":
    main()
