def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle

    return left


arr = [1, 3, 4 ,5, 7]
print(searchInsert(arr, 7))
