def sortedSquares(nums: list[int]) -> list[int]:
    def Merge_Sort(A, p, r):
        if p < r:
            q = (p + r) // 2
            Merge_Sort(A, p, q)
            Merge_Sort(A, q + 1, r)
            Merge(A, p, q, r)

    def Merge(A, p, q, r):
        left = A[p: q + 1]
        right = A[q + 1: r + 1]
        import math
        left.append(math.inf)
        right.append(math.inf)
        i, j = 0, 0
        for k in range(p, r + 1):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1

    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

    Merge_Sort(nums, 0, len(nums) - 1)
    return nums
