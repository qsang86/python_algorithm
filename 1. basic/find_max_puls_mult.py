input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):

    result = 0
    for number in array:
        if number <= 1 or result == 0:
            result += number
        else:
            result *= number

    return result


result = find_max_plus_or_multiply(input)
print(result)