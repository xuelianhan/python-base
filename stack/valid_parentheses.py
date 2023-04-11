class ValidParentheses:
    def __init__(self):
        pass

    def isValidV2(self, s: str) -> bool:
        if not s or len(s) < 2:
            return False
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return not stack

    def isValidV1(self, s: str) -> bool:
        if not s or len(s) < 2:
            return False
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif not stack or stack.pop() != c:
                return False
        return not stack

    def isValid(self, s: str) -> bool:
        if not s or len(s) < 2:
            return False
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if c == ')' and last != '(':
                    return False
                if c == '}' and last != '{':
                    return False
                if c == ']' and last != '[':
                    return False
        return not stack

instance = ValidParentheses()
#s = "(]"
s = "()[]{}"
res = instance.isValidV2(s)
print(res)



