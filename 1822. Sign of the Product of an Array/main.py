def arraySign(nums: list[int]) -> int:
    product = 1
    i, j = 0, len(nums) - 1
    while i < j:
        product *= nums[i] * nums[j]
        i += 1
        j -= 1
    product *= nums[i] if len(nums) % 2 == 1 else None
    if product == 0:
        return 0
    elif product > 0:
        return 1
    else:
        return -1


print(arraySign([-1, -2, -3, -4, 3, 2, 1]))
