#Hash
#문자열을 고정된 길이의 데이터
#dictionary or blockchain 에 사용

#sorting
##Bubble Sort
###위치를 n과 n-1을 비교하며 정렬

input = [4, 6, 2, 9, 1]


def bubble_sort(array):

    n = len(array)

    for i in range(n-1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
                
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!