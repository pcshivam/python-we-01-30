def check_even(num):
    for i in num:
        if i % 2 == 0:
            print(i)

num = list(range(1,21))
check_even(num)

list1 = []

def check_odd(num):
    for n in num:
        if n%2 != 0:
            list1.append(n)
    return list1

num = list(range(1,31))

print(check_odd(num))