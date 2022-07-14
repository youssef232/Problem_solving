def isAnagram(s: str, t: str) -> bool:
    mydict = {}
    if len(s) > len(t):
        return False
    for i in s:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1

    for i in range(len(t)):
        if t[i] not in mydict:
            return False
        elif mydict[t[i]] == 0:
            return False
        else:
            mydict[t[i]] -= 1

    return True


print(isAnagram("anagram", "nagaram"))
