def subtractProductAndSum(n: int) -> int:
    sum, product = 0, 1
    while n != 0:
        digit = n % 10
        sum += digit
        product *= digit
        n = int(n/10)

    return product - sum


print(subtractProductAndSum(33))