import csv

def open_file(file_name):
    '''
    open file, replace \n with empty string, convert to int or None
    '''
    lst = []
    with open(file_name, 'r') as f:
        csv_reader = csv.reader(f)
        for line in f:
            s = line.replace('\n', '')
            s = None if s is '' else (int(s))
            lst.append(s)
    return lst

def part_1():
    data = open_file('./day_1.csv')
    all_calories = []
    each_elf = []
    for i, row in enumerate(data):
        if row:
            each_elf.append(row)
        else:
            all_calories.append(sum(each_elf))
            each_elf = []
    return max(all_calories)

def part_2():
    data = open_file('./day_1.csv')
    all_calories = []
    each_elf = []
    for i, row in enumerate(data):
        if row:
            each_elf.append(row)
        else:
            all_calories.append(sum(each_elf))
            each_elf = []
    all_calories.sort(reverse=True)
    return sum(all_calories[:3])


if __name__ == '__main__':
    print(part_1())
    print(part_2())