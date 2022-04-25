def largestPerimeter(nums: list[int]) -> int:
    nums.sort(reverse=True)

    for i in range(len(nums) - 2):
        if nums[i] < (nums[i + 1] + nums[i + 2]):
            return nums[i] + nums[i + 1] + nums[i + 2]

    return 0


print(largestPerimeter([6, 1, 6, 5, 8, 4]))
