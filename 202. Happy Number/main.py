def isHappy(n: int) -> bool:
    mySet = set()
    while n != 1 and n not in mySet:
        mySet.add(n)
        n =sum_num(n)
    return n == 1


def sum_num(n):
    total_square_sum = 0
    while n > 0:
        n, reminder = divmod(n, 10)
        total_square_sum += reminder ** 2
    return total_square_sum

print(isHappy(149))
