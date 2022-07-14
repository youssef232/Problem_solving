def firstUniqChar(s: str) -> int:
    mydict = {}
    for i in s:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1

    for i in range(len(s)):
        if mydict[s[i]] == 1:
            return i

    return -1


print(firstUniqChar("aabb"))
