def sortedSquares(nums: list[int]) -> list[int]:
    i, j = 0, len(nums) - 1
    answer = [0] * len(nums)
    for k in range(-1, -(len(nums) + 1), -1):
        if abs(nums[i]) > abs(nums[j]):
            answer[k] = nums[i] ** 2
            i += 1
        else:
            answer[k] = nums[j] ** 2
            j -= 1

    return answer


nums = [-4, -1, 2, 3, 10]
print(sortedSquares(nums))
