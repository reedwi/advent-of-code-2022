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

class Rope:
    head = []
    tail = []
    visited = [(0,0)]

    def __init__(self, head, tail) -> None:
        self.head = head
        self.tail = tail
    
    def parse_move(self, direction, distance):
        tail_x, tail_y = self.tail[0], self.tail[1]

        if direction == 'U':
            self.head[1] += distance
            # visited_range = self.head[1] - (tail_y + 1)
            # print(visited_range)
            self.visited.extend([(self.head[0], i) for i in range(tail_y + 1, self.head[1])])

        elif direction == 'D':
            self.head[1] -= distance
            # visited_range = tail_y - (self.head[1] + 1)
            # print(visited_range)
            self.visited.extend([(self.head[0], i) for i in reversed(range(self.head[1] + 1, tail_y))])

        elif direction == 'R':
            self.head[0] += distance
            # visited_range = self.head[0] - (tail_x + 1)
            # print(visited_range)
            self.visited.extend([(i, self.head[1]) for i in range(tail_x + 1, self.head[0])])

        elif direction == 'L':
            self.head[0] -= distance
            # visited_range = tail_x - (self.head[0] + 1)
            # print(visited_range)
            self.visited.extend([(i, self.head[1]) for i in reversed(range(self.head[0] + 1, tail_x))])
    
    def do_move(self, direction, distance):
        tail = self.tail.copy()
        self.parse_move(direction=direction, distance=distance)
        head = self.head.copy()
        
        head_x, head_y = head[0], head[1]
        tail_x, tail_y = tail[0], tail[1]

        if abs(head_x - tail_x) >= 2 or abs(head_y - tail_y) >= 2:
            self.tail[0], self.tail[1] = self.visited[-1:][0]


    def solution(self):
        return len(set(self.visited))


def part_1():
    data = open_file('day_9.txt')
    rope = Rope(head=[0, 0], tail=[0, 0])
    for i, row in enumerate(data):
        rope.do_move(direction=row[0], distance=int(row[1]))
        # print(rope.head)
        # print(rope.tail)
        # print(rope.visited)
        # if i == 5:
        #     break

    return rope.solution()

def part_2():
    pass

if __name__ == '__main__':
    solution_1 = part_1()
    print(solution_1)
    