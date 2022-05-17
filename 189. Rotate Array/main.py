def rotate(nums: list[int], k: int):
    tempList = [0] * len(nums)
    j = k % len(nums)
    for i in range(len(nums) - k):
        tempList[j] = nums[i]
        j += 1

    j = 0
    for i in range(len(nums) - k, len(nums)):
        tempList[j] = nums[i]
        j += 1

    nums = tempList.copy()
    return nums


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(rotate(nums, k))



if __name__ == "__main__":
    main()


