from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np

def cartesian(*arrays):
    mesh = np.meshgrid(*arrays)  # standard numpy meshgrid
    dim = len(mesh)  # number of dimensions
    elements = mesh[0].size  # number of elements, any index will do
    flat = np.concatenate(mesh).ravel()  # flatten the whole meshgrid
    reshape = np.reshape(flat, (dim, elements)).T  # reshape and transpose
    return reshape

def prepare_caves(caves):
    new_caves = []
    for cave in caves:
        first = cave.split('-')[0]
        second = cave.split('-')[1]
        if second=='start' or first=='end':
            cave = second+'-'+first
            temp = first
            first = second
            second = temp

        new_caves.append(cave)
        if cave[0:5]!='start' and cave[-3:]!='end':
            new_caves.append(second+'-'+first)
    return np.array(new_caves)


def get_repeat_count(el, first):
    repeat_count = 0
    for x in first:
        if x==el:
            repeat_count += 1
    return repeat_count


def check_incomplete(first,second):
    first_split = first.split('-')
    second_split = second.split('-')
    double_new_char = second_split[0] + second_split[0]
    double_new2_char = second_split[1] + second_split[1]
    allowed_to_visit_small = True
    for el in first_split:
        if not el.isupper() and get_repeat_count(el,first_split)==2:
            allowed_to_visit_small = False
            break
    if first != second and second[0:5] != 'start' and first[0:5] == 'start' and first_split[len(first_split) - 1] == second_split[0] and second[-3:] != 'end' and ((double_new_char not in first or double_new_char.isupper() or allowed_to_visit_small) and (double_new2_char not in first or double_new2_char.isupper() or allowed_to_visit_small)):
        return True
    else:
        return False


def check_double_lowercase_count(new_path):
    paths = new_path.split('-')
    double_count = 0
    for path in paths:
        if get_repeat_count(path,paths)>1 and not path.isupper():
            paths.remove(path)
            double_count += 1
    return double_count


def find_paths(caves, new_list, paths):
    a = cartesian(new_list,caves)
    incomplete_paths = []
    for c in a:
        incomplete = check_incomplete(c[0], c[1])
        if incomplete:
            incomplete_paths.append(c)
        if c[0][0:5]=='start' and c[1][-3:]=='end' and c[0].split('-')[len(c[0].split('-'))-1] == c[1].split('-')[0]:
            paths.append(c)

    if len(incomplete_paths)>0:
        new_list = []
        for path in incomplete_paths:
            new_list.append(path[0]+path[1])
        new_list = np.array(new_list)
        new_list, paths = find_paths(caves, new_list, paths)
    new_paths = []
    for path in paths:
        new_path = path[0]+path[1]
        if check_double_lowercase_count(new_path)<2:
            new_paths.append(new_path)
    return new_list, new_paths

def main():
    print(datetime.now())
    dataset = read_file('real_dataset.txt')
    new_dataset = []
    for row in dataset:
        new_dataset.append(row.replace('\n', ''))
    caves = np.array(new_dataset)
    caves = prepare_caves(caves)
    print(caves)
    new_list, paths = find_paths(caves,caves, [])
    print(paths)
    print('total path count is {}'.format(len(paths)))
    # print(new_list)
    print(datetime.now())

if __name__ == "__main__":
    main()

#
#
# start,dc,end
# start,HN,end
# start,HN,dc,end
# start,kj,dc,end
# start,dc,HN,end
# start,kj,HN,end
# start,kj,HN,dc,end
# start,HN,kj,dc,end
# start,HN,dc,HN,end
# start,kj,dc,HN,end
# start,HN,kj,HN,end
# start,HN,kj,HN,dc,end
# start,kj,HN,dc,HN,end
# start,HN,kj,dc,HN,end
# start,dc,HN,kj,HN,end
# start,HN,kj,HN,dc,HN,end
# start,HN,dc,HN,kj,HN,end
#
# start,HN,dc,kj,HN,end
# start,dc,kj,HN,end
#


