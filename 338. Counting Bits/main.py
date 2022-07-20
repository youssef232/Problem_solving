def countBits(n: int) -> list[int]:
    arr = [0] * (n + 1)
    for i in range(n + 1):
        binary = bin(i)
        count = binary.count('1')
        arr[i] = count
    return arr


print(countBits(2))
