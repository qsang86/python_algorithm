def adv_mergesort(s, low, high):
    if(low < high):
        mid = (low+high)//2
        adv_mergesort(s, low, mid)
        adv_mergesort(s, mid+1, high)
        return adv_merge(s, low, mid, high)

def adv_merge(s, low, mid, high ):
    new_list = []
    i = low
    j = mid+1

    while(i<=mid and j<=high):
        if(s[i] < s[j]):
            new_list.append(s[i])
            i += 1
          #  print(new_list)
        elif(s[j] < s[i]):
            new_list.append(s[j])
            j += 1
          #  print(new_list)


    if(i<=mid):
        new_list.extend(s[i:mid+1])
    else:
        new_list.extend(s[j:high+1])

    for k in range(low, high+1):
        s[k] = new_list[k-low]

    #print(new_list)
    return new_list


def main():
    alist = [27, 10, 12, 20, 25, 13, 15, 22]
    merg = adv_mergesort(alist, 0, len(alist)-1)
    print(merg)



if __name__ == "__main__":
    main()
