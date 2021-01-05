def get_max(s):
    max = 0
    for num in range(0, len(s)):
        if(max < s[num]):
            max = s[num]

    return max


def main():
    input = [3, 5, 6, 1, 2, 4]
    result = get_max(input)
    print(result)

if __name__ =="__main__":
    main()