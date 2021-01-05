finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    
    sorted_num = sorted(numbers)
    low = 0
    high = len(sorted_num) - 1

    while(low <= high):
        mid = (low+high)//2

        if(target == sorted_num[mid]):

            return True
        elif(target > sorted_num[mid]):
            low = mid + 1
        else:
            high = mid - 1


    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)

print(result)