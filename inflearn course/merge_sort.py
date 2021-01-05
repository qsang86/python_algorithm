

def mergesort(bin_list):
    n = len(bin_list)

    if(n <= 1):
        return bin_list
    else:
        mid = n // 2
        list1 = mergesort(bin_list[0:mid])
        list2 = mergesort(bin_list[mid:n])
        return merge(list1, list2)

def merge(list1, list2):
    i = 0
    j = 0
    new_list = []
    while(i < len(list1) and j < len(list2)):
        if(list1[i] < list2[j]):
            new_list.append(list1[i])
            i += 1
        elif(list1[i] > list2[j]):
            new_list.append(list2[j])
            j += 1

    #if(i < len(list1)):
    #    new_list += list1[i:len(list1)]
    #elif(j < len(list2)):
    #    new_list += list2[j:len(list2)]

    if(i < len(list1)):
        new_list.extend(list1[i:])
    else: new_list.extend(list2[:j])

    return new_list

def main():
    aList = [27, 10, 12, 20, 25, 13, 15, 22]
    merg = mergesort(aList)
    print(merg)

if __name__ == "__main__":
    main()

