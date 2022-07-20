def reverseBits(n: int) -> int:
    reversedNumber = 0
    for i in range(32):
        reversedNumber = (reversedNumber << 1) + (n & 1)
        n = n >> 1
    return reversedNumber


