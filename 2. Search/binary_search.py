finding_target = 13
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!

    #calculate time complexity
    #O(log(N))
    find_count = 0
    high = len(array)-1
    low = 0
    while low <= high:

        find_count += 1

        mid = (low+high)//2
        if target == array[mid]:
            print(find_count)
            return True
            break
        elif target > array[mid]:
            low = mid+1
        else:
            high = mid-1

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)