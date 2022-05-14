def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1


print(binary_search([5 , 10 , 12, 33, 55], 10))