## All code will go here

def add(string_numbers):
    if string_numbers == "":
        return 0

    numbers_list = string_numbers.replace("\n", ",").split(",")
    numbers_sum = sum(map(int, numbers_list))

    return numbers_sum