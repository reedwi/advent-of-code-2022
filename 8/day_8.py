# ENDED HERE. HAVE READ PROMPT FOR DAY 7 BUT HAVENT ATTEMPTED YET
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
                lst.append(s)
    return lst



def part_1():
    data = open_file('day_8.txt')
    visible = []
    total_rows = len(data)
    for i, row in enumerate(data):
        row_len = len(row)
        if i == 0 or i == total_rows - 1:
            visible.extend(row)
            continue

        for ii, value in enumerate(row):
            if ii == 0 or ii == row_len - 1:
                visible.append(value)
            else:
                # check value above
                if max([row_column[ii] for row_column in data[:i]]) < value:
                    visible.append(value)
                # check value below
                
                elif max([row_column[ii] for row_column in data[i+1:]]) < value:
                    visible.append(value)
                # check value left
                elif max(data[i][:ii]) < value:
                    visible.append(value)
                # check value right
                elif max(data[i][ii+1:]) < value:
                    visible.append(value)
    return len(visible)

def part_2():
    data = open_file('day_8.txt')
    scores = []
    total_rows = len(data)
    for i, row in enumerate(data):
        if i == 0 or i == total_rows - 1:
            continue
        for ii, value in enumerate(row):
            tree = data[i][ii]

            above = [row_column[ii] for row_column in data[:i]]
            below = [row_column[ii] for row_column in data[i+1:]]
            left = [num for num in data[i][:ii]]
            right = [num for num in data[i][ii+1:]]
            all_around = [above, below, left, right]
            print(tree)
            score = 1
            for direction in all_around:
                print(direction)
                tracker = 0
                for iii, height in enumerate(direction):
                    print(f'height: {height}')
                    if height < tree:
                        tracker += 1
                    elif height >= tree:
                        tracker += 1
                        break
                score *= tracker
            # return score
            scores.append(score)

    return scores

if __name__ == '__main__':
    solution_1 = part_1()
    solution_2 = part_2()
    print(solution_1)
    print(solution_2)