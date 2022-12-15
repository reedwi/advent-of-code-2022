# ENDED HERE. HAVE READ PROMPT FOR DAY 7 BUT HAVENT ATTEMPTED YET
from collections import defaultdict
from pprint import pprint

def open_file(file_name):
    '''
    open file, replace \n with empty string, convert to int or None
    '''
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            if line:
                s = line.replace('\n', '')
                lst.append(s.split(' '))
    return lst



def part_1():
    data = open_file('day_7.txt')
    file_path = []
    directory_sizes = defaultdict(int)
    for i, line in enumerate(data):
        if line[1] == 'cd':
            if line[2] == '..':
                file_path.pop()
            else:
                file_path.append(line[2])
                
        elif line[1] == 'ls':
            continue

        else:
            try:
                file_size, name = int(line[0]), line[1]
                for i, file in enumerate(file_path, start=1):
                    directory_sizes['/'.join(file_path[:i])] += file_size
            except:
                continue
    total = 0
    for key, value in directory_sizes.items():
        if value <= 100000:
            total += value

    return total, directory_sizes

def part_2(directory_sizes):
    total_space = 70000000
    update_size = 30000000
    used_space = directory_sizes['/']
    free_space = total_space - used_space
    space_needed = update_size - free_space
    possibles = list(directory_sizes.values())
    options = []
    for value in possibles:
        if value > space_needed:
            options.append(value)
    return min(options)

if __name__ == '__main__':
    total, directory_sizes = part_1()
    smallest_size = part_2(directory_sizes)
    print(total)
    print(smallest_size)