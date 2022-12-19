import sys

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
    data = open_file('day_10.txt')
    power = {1 : 1, 2 : 1}
    x = 1
    cycle = 1
    powers = []
    last_iteration = None
    for i, row in enumerate(data, start=1):
        powers.append(x)
        if i in power:
            continue
    

        if row[0] == 'addx':
            powers.append(x)
            x += int(row[1])
        # print(x)

    solution = 0
    for i in (20, 60, 100, 140, 180, 220):
        solution += powers[i-1]*i
    
    return solution

if __name__ == '__main__':
    solution_1 = part_1()
    print(solution_1)

        