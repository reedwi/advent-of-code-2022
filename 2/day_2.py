
scoring_amounts_1 = {
    'X': {
        'A': 4,
        'B': 1,
        'C': 7
    },
    'Y': {
        'A': 8,
        'B': 5,
        'C': 2
    },
    'Z': {
        'A': 3,
        'B': 9,
        'C': 6
    },
}

scoring_amounts_2 = {
    'X': {
        'A': 3,
        'B': 1,
        'C': 2
    },
    'Y': {
        'A': 4,
        'B': 5,
        'C': 6
    },
    'Z': {
        'A': 8,
        'B': 9,
        'C': 7
    },
}

def open_file(file_name):
    '''
    open file, replace \n with empty string, convert to int or None
    '''
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            s = line.replace('\n', '')
            lst.append(s.split(' '))
    return lst

def part_1():
    data = open_file('day_2.txt')
    score = 0
    for game_results in data:
        score += scoring_amounts_1[game_results[1]][game_results[0]]
    return score

def part_2():
    data = open_file('day_2.txt')
    score = 0
    for game_results in data:
        score += scoring_amounts_2[game_results[1]][game_results[0]]
    return score

if __name__ == '__main__':
    print(part_1())
    print(part_2())