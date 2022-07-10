def twoSum(nums: list[int], target: int) -> list[int]:
    mydict = {}
    for index, value in enumerate(nums):
        reminder = target - value
        if reminder in mydict:
            return [mydict[reminder], index]
        else:
            mydict[value] = index


nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
