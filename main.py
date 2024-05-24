## All code will go here

def extract_delimiter_and_number_string(string_numbers):
    delimiter = ","

    if string_numbers[:2] == "//":
        delimiter = string_numbers[2]
        string_numbers = string_numbers[3:]
    return string_numbers, delimiter

def get_numbers_list(numbers_string, delimiter):
    numbers_string_list = numbers_string.replace("\n", delimiter).split(delimiter)
    numbers_list = list(map(int, numbers_string_list))
    return numbers_list

def add(string_numbers):
    if string_numbers == "":
        return 0
    
    string_numbers, delimiter = extract_delimiter_and_number_string(string_numbers)
    numbers_list = get_numbers_list(string_numbers, delimiter)

    numbers_sum = sum(numbers_list)
    return numbers_sum