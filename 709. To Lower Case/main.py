def toLowerCase(s: str) -> str:
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            s = s.replace(s[i], chr(ord(s[i]) + 32))
    return s


print(toLowerCase("SAID"))
