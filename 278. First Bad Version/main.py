def firstBadVersion( n: int) -> int:
    start, end = 1, n
    while start < end:
        # middle = (start + end) // 2  caused overflow
        middle = start + (end - start) // 2
        if isBadVersion(middle):
            end = middle
        else:
            start = middle + 1
    return start
