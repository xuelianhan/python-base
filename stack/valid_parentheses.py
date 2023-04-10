class ValidParentheses:
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