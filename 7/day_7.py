# ENDED HERE. HAVE READ PROMPT FOR DAY 7 BUT HAVENT ATTEMPTED YET

def open_file(file_name):
    '''
    open file, replace \n with empty string, convert to int or None
    '''
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            if line:
                s = line.replace('\n', '')
                lst.append(s)
    return lst


def part_1():
    data = open_file('day_7.txt')
    print(data)

def part_2():
    data = open_file('day_4.txt')
    count = 0
    for row in data:
        if set(row[0]) & set(row[1]):
            count += 1
    return count

if __name__ == '__main__':
    print(part_1())
    # print(part_2())