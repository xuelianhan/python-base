'''
LC1249, Medium, frequency=282
'''
class MinimumRemoveMakeValidParentheses:
    def __init__(self):
        pass

    #Understandind the following solution
    def minRemoveToMakeValidV1(self, s: str) -> str:
        if len(s) == 0:
            return ''
        stack = []
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == '(':
                stack.append(i)
            elif s_list[i] == ')':
                if len(stack) == 0:
                    s_list[i] = ''
                else:
                    stack.pop()
        for i in stack:
            s_list[i] = ''
        return ''.join(s_list)

    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 0:
            return ""
        stack = []
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] == '(':
                stack.append(i)
            elif s_list[i] == ')':
                if not stack:
                    s_list[i] = '*'
                else:
                    stack.pop()
        for i in stack:
            s_list[i] = '*'
        res = ""
        for c in s_list:
            if c != '*':
                res += c
        return res

instance = MinimumRemoveMakeValidParentheses()
#s = "(]"
s = "lee(t(c)o)de)"
res = instance.minRemoveToMakeValidV1(s)
print(res)