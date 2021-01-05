input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    #calc on the length of array
    for num in array:

        #calc on if
        if(number == num):

            #N*1 = N
            return True
    return False

#>>O(N)

result = is_number_exist(3, input)
print(result)