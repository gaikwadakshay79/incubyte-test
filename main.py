def extract_delimiter_and_number_string(string_numbers):
    delimiter = ","
    if string_numbers.startswith("//"):
        delimiter = string_numbers[2]
        string_numbers = string_numbers[4:]
    return string_numbers, delimiter

def get_numbers_list(numbers_string, delimiter):
    numbers_string_list = numbers_string.replace("\n", delimiter).split(delimiter)
    return list(map(int, numbers_string_list))

def validate_input_numbers(numbers_list):
    negative_numbers = [number for number in numbers_list if number < 0]
    if negative_numbers:
        exception_message_list = []
        for nnumber in negative_numbers:
            exception_message_list.append("negative numbers not allowed {}".format(nnumber))
        if exception_message_list:
            raise ValueError(",".join(exception_message_list))
        
def get_result(delimiter, numbers_list):
    if delimiter == "*":
        result = 1
        for number in numbers_list:
            if number == 0:
                return 0
            result *= number
        return result
    return sum(numbers_list)

def add(string_numbers):
    if not string_numbers:
        return 0
    
    string_numbers, delimiter = extract_delimiter_and_number_string(string_numbers)
    numbers_list = get_numbers_list(string_numbers, delimiter)
    validate_input_numbers(numbers_list)
    return get_result(delimiter, numbers_list)
