def location(bin_list, low, high):
    if(low > high):
        return 0
    else:
        mid = (low+high)//2
        if(x == bin_list[mid]):
            return x
        elif(x < bin_list[mid]):
            return location(bin_list, low, mid-1)
        else:
            return location(bin_list, mid+1, high)

list = [-1, 10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45]
x = 18
loc = location(list, 0, len(list)-1)
print(loc)

