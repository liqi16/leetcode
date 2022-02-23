class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        if s == "": #***
            return True
        for c in s:
            if c in ["(","[","{"]:
                stack.append(c)
            else:
                if len(stack) > 0: #***
                    top = stack.pop(-1)
                    if c == ")":
                        if top != "(":
                            return False
                    elif c == "]":
                        if top != "[":
                            return False
                    elif c == "}":
                        if top != "{":
                            return False
                    else:
                        return False
                else:
                    return False
        if len(stack) > 0: #***
            return False
        else:
            return True
