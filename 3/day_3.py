
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

def chars_to_ints(chars):
    new_ints = []
    for char in chars:
        if char.islower():
            val = ord(char) - 96
        else:
            val = ord(char.lower()) - 70
        new_ints.append(val)
    return new_ints

def part_1():
    data = open_file('day_3.txt')
    total_value = 0
    for row in data:
        deciphered_vals = chars_to_ints(chars=row)
        compartment_1 = deciphered_vals[:len(deciphered_vals)//2]
        compartment_2 = deciphered_vals[len(deciphered_vals)//2:]
        shared_item = list(set(compartment_1).intersection(compartment_2))
        total_value += shared_item[0]

    return total_value

def sliding_window(data, window_size):
    common_elements = []
    for i in range(len(data) - window_size + 1):
        if i % 3 != 0:
            continue
        sub_data = data[i: i + window_size]
        common_element = list(set(sub_data[0]).intersection(sub_data[1], sub_data[2]))
        common_elements.append(common_element[0])
    return common_elements

def part_2():
    data = open_file('day_3.txt')
    converted_data = []
    for row in data:
        deciphered_vals = chars_to_ints(chars=row)
        converted_data.append(deciphered_vals)

    common_elements = sliding_window(data=converted_data, window_size=3)
    return sum(common_elements)

if __name__ == '__main__':
    print(part_1())
    print(part_2())