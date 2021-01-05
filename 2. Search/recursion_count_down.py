def count_down(number):

    if number == 0:
        print(0)
    elif number >=  1:
        print(number)
        count_down(number-1)

count_down(60)