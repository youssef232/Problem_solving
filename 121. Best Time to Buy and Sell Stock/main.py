def maxSubArray(nums: list[int]) -> int:
    output = maxSum = nums[0]

    for i in range(1, len(nums)):
        maxSum = max(nums[i], maxSum + nums[i])
        output = max(output, maxSum)

    return output


nums = [5,4,-1,7,8]
print(maxSubArray(nums))
