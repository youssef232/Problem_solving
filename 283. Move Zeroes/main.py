def moveZeroes(nums: list[int]) -> None:
    numberOfZero = 0
    i = 0
    for j in range(len(nums)):
        if nums[j] == 0:
            numberOfZero += 1
        else:
            nums[i] = nums[j]
            i += 1
    for j in range(-1, -(numberOfZero + 1), -1):
        nums[j] = 0
