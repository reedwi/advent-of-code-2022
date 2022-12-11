def open_file(file_name):
    '''
    open file, replace \n with empty string, convert to int or None
    '''
    lst = []
    with open(file_name, 'r') as f:
        for line in f:
            if line:
                lst.append(line)
    return lst

def part_1():
    data = open_file('day_6.txt')
    string_series = data[0]
    for i in range(3, len(string_series)):
        subset = string_series[i-3:i+1]
        if len(set(subset)) == 4:
            return i+1

def either_part(char_amount: int):
    data = open_file('day_6.txt')
    string_series = data[0]
    amount = char_amount - 1
    for i in range(amount, len(string_series)):
        subset = string_series[i-amount:i+1]
        if len(set(subset)) == char_amount:
            return i+1

if __name__ == '__main__':
    print(part_1())
    print(either_part(char_amount=14))