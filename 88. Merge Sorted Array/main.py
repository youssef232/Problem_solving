import math


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    right = nums1[: m]
    right.append(math.inf)
    nums2.append(math.inf)
    i = 0; j = 0
    for k in range(m + n):
        if right[i] <= nums2[j]:
            nums1[k] = right[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1

    print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1,m, nums2, n)
