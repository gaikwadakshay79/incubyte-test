## All code will go here

def extract_delimiter_and_number_string(string_numbers):
    delimiter = ","

    if string_numbers[:2] == "//":
        delimiter = string_numbers[2]
        string_numbers = string_numbers[3:]
    return delimiter, string_numbers


def add(string_numbers):
    if string_numbers == "":
        return 0
    
    delimiter, string_numbers = extract_delimiter_and_number_string(string_numbers)

    numbers_list = string_numbers.replace("\n", delimiter).split(delimiter)
    numbers_sum = sum(map(int, numbers_list))

    return numbers_sum