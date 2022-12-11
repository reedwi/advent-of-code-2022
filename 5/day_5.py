from collections import deque
starting_stack = {
    1: deque(['N', 'H', 'S', 'J', 'F', 'W', 'T', 'D']),
    2: deque(['G', 'B', 'N', 'T', 'Q', 'P', 'R', 'H']),
    3: deque(['V', 'Q', 'L']),
    4: deque(['Q', 'R', 'W', 'S', 'B', 'N']),
    5: deque(['B', 'M', 'V', 'T', 'F', 'D', 'N']),
    6: deque(['R', 'T', 'H', 'V', 'B', 'D', 'M']),
    7: deque(['J', 'Q', 'B', 'D']),
    8: deque(['Q', 'H', 'Z', 'R', 'V', 'J', 'N', 'D']),
    9: deque(['S', 'M', 'H', 'N', 'B'])
}
# [N] [G]                     [Q]    
# [H] [B]         [B] [R]     [H]    
# [S] [N]     [Q] [M] [T]     [Z]    
# [J] [T]     [R] [V] [H]     [R] [S]
# [F] [Q]     [W] [T] [V] [J] [V] [M]
# [W] [P] [V] [S] [F] [B] [Q] [J] [H]
# [T] [R] [Q] [B] [D] [D] [B] [N] [N]
# [D] [H] [L] [N] [N] [M] [D] [D] [B]

def open_file(file_name):
    '''
    open file, replace \n with empty string, convert to int or None
    '''
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            if line:
                s = line.replace('\n', '')
                split_row = s.split(' ')
                amount, from_column, to_column = split_row[1], split_row[3], split_row[5]
                lst.append([int(amount), int(from_column), int(to_column)])
    return lst

def part_1():
    data = open_file('day_5.txt')
    for move in data:
        for i in range(move[0]):
            val = starting_stack[move[1]].popleft()
            starting_stack[move[2]].appendleft(val)
    
    top_crates = ''
    for column, stack in starting_stack.items():
        top_crates += stack[0]
    return top_crates
    # for move in data:


def part_2():
    data = open_file('day_5.txt')
    for move in data:
        intermediary_queue = deque()
        for i in range(move[0]):
            val = starting_stack[move[1]].popleft()
            intermediary_queue.appendleft(val)
        
        starting_stack[move[2]].extendleft(intermediary_queue)
        intermediary_queue.clear()
    
    top_crates = ''
    for column, stack in starting_stack.items():
        top_crates += stack[0]
    return top_crates

if __name__ == '__main__':
    # print(part_1())
    print(part_2())