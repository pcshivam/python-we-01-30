def check_even(num):
    for i in num:
        if i%2 == 0:
            print(i)

num = list(range(1,21))

check_even(num)