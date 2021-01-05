def find_prime_list_under_number(number):
    result = []

    if(number <= 1):
        return 0
    else:
        for i in range(2, number+1):
            checker = True
            for j in range(2, i):
                if(i%j == 0):
                    checker = False
                    break
            if(checker == True):
                result.append(i)


    return result


def main():
    input = 20
    result = find_prime_list_under_number(input)
    print(result)


if __name__ =="__main__":
    main()


    