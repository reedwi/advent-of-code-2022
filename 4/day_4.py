
def open_file(file_name):
    '''
    open file, replace \n with empty string, convert to int or None
    '''
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            if line:
                s = line.replace('\n', '')
                split_row = s.split(',')
                split_row[0] = list(range(int(split_row[0].split('-')[0]), int(split_row[0].split('-')[1]) + 1, 1))
                split_row[1] = list(range(int(split_row[1].split('-')[0]), int(split_row[1].split('-')[1]) + 1, 1))
                lst.append(split_row)
    return lst

def part_1():
    data = open_file('day_4.txt')
    count = 0
    for row in data:
        if set(row[0]).issubset(set(row[1])) or set(row[1]).issubset(set(row[0])):
            count += 1
    return count

def part_2():
    data = open_file('day_4.txt')
    count = 0
    for row in data:
        if set(row[0]) & set(row[1]):
            count += 1
    return count

if __name__ == '__main__':
    print(part_1())
    print(part_2())