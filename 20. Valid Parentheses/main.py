def isValid(s: str) -> bool:
    if len(s) == 1:
        return False
    stack = []
    for i in s:
        if i == "{" or i == "[" or i == "(":
            stack.append(i)
        elif len(stack) == 0:
            return False
        else:
            if i == "}" and stack[-1] == "{":
                stack.pop()

            elif i == "]" and stack[-1] == "[":
                stack.pop()

            elif i == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False

    return True if len(stack) == 0 else False


print(isValid("}{"))
