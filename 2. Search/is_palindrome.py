
def is_palindrome(string):
    mid = len(string)//2
    #print(string[mid])
    for i in range(len(string)):
        if(string[i] != string[len(string) - 1 - i]):
            return False

    return True

def is_palindrome_re(string):
    mid = len(string)//2
    if string[0] != string[-1]:
        return False
    if len(string) == 1:
        return True
    else:
        print(string)
        string = string[1:-1]
        return is_palindrome_re(string)


    return False

def main():
    input = "abcba"
    print("non recursion: ", is_palindrome(input))
    print("recursoin: ", is_palindrome_re(input))

if __name__ == "__main__":
    main()