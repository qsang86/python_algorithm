input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    length = len(string)
    count_one = 0
    count_zero = 0

    for i in range(0, length):
        if(string[i] == '0'):
            count_zero += 1
        elif(string[i] == '1'):
            count_one += 1

    if(count_zero > count_one):
        return count_one
    else:
        return count_zero



result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)