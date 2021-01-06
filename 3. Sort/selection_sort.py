input = [4, 6, 2, 9, 1]
input2 = [4, 3, 2, 5, 1, 6, 1]

def selection_sort(array):
  

    for i in range(len(array) - 1):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j

        if min != i:
            array[min], array[i] = array[i], array[min]


    return array

def selection_sort_2(array):

    for i in range(len(array)-1):
        min_index = i
        for j in range(len(array)-i):
            if array[i+j] < array[min_index]:
                min_index = i+j

        array[i], array[min_index] = array[min_index], array[i]



selection_sort(input)
print(input) 

selection_sort_2(input2)
print(input2)