# 20. Valid Parentheses

def isValid(s):
    # length = len(s)
    # if length == 1:
    #     return False
    #
    # for letter in range(int(length/2)):
    #     if s[letter] == "[":
    #         if "]" != s[letter+1] and "]" != s[length-1-letter]:
    #             return False
    #     elif s[letter] == "(":
    #         if ")" != s[letter+1] and ")" != s[length-1-letter]:
    #             return False
    #     elif s[letter] == "{":
    #         if "}" != s[letter+1] and "}" != s[length-1-letter]:
    #             return False
    #
    # return True

    length = len(s)

    def check(start, end):
        if s[letter] == start:
            try:
                if (s.index(end) - letter) % 2 == 0:
                    print("False")
                    return False
            except ValueError:
                return False

    for letter in range(int(length/2)):
        if s[letter] == "}" or s[letter] == ")" or s[letter] == "]":
            if check("}", "{") is False or check(")", "(") is False or check("]", "[") is False:
                return False
        elif check("{", "}") is False or check("(", ")") is False or check("[", "]") is False:
            return False

    return True


print(isValid("]"))
