## All code will go here

def add(string_numbers):
    if string_numbers == "":
        return 0
    
    delimiter = ","

    if string_numbers[:2] == "//":
        delimiter = string_numbers[2]
        string_numbers = string_numbers[3:]

    numbers_list = string_numbers.replace("\n", delimiter).split(delimiter)
    numbers_sum = sum(map(int, numbers_list))

    return numbers_sum