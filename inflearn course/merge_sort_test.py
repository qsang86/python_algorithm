def mergesort(s):
    n = len(s)
    if(n <= 1):
        return s
    else:
        mid = n//2
        x = mergesort(s[0:mid])
        y = mergesort(s[mid:n])
        return merge(x, y)

def merge(x, y):
    i = 0
    j = 0
    new_list = []

    while(i < len(x) and j <len(y)):
        if(x[i] < y[j]):
            new_list.append(x[i])
            i+=1
        elif(x[i] > y[j]):
            new_list.append(y[j])
            j += 1

    if(i < len(x)):
        new_list += x[i:len(x)]
    elif(j < len(y)):
        new_list += y[j:len(y)]
    return new_list

alist = [0, 8, 4, 6, 7, 9, 21, 23]
print(mergesort(alist))
