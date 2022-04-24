def hammingWeight(n: int) -> int:
    ones = 0
    while n != 0:
        ones += (n & 1)
        n >>= 1
    return ones


print(hammingWeight(0b0000000000000000000000000001011))

