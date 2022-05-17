def rotate(nums: list[int], k: int):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

