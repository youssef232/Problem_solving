def canConstruct(ransomNote: str, magazine: str) -> bool:
    mydict = {}
    for i in magazine:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1

    for i in ransomNote:
        if i not in mydict:
            return False
        elif mydict[i] == 0:
            return False
        else:
            mydict[i] -= 1

    return True


print(canConstruct('aa', 'aab'))
