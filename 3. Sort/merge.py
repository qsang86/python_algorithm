array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

def merge_rest(array_a, index_a, output):
    if index_a < len(array_a):
        for i in range(index_a, len(array_a)):
            add_ele = array_a[i]
            output.append(add_ele)

    return output

def merge(array1, array2):
    # 이 부분을 채워보세요!
    output = []
    index1 = 0
    index2 = 0

    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] < array2[index2]:
            output.append(array1[index1])
            index1 += 1
        else:
            output.append(array2[index2])
            index2 += 1

    rest_output1 = merge_rest(array1, index1, output)
    rest_output2 = merge_rest(array2, index2, output)
    if len(rest_output1) > len(rest_output2):
        return rest_output1

    return rest_output2




print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!