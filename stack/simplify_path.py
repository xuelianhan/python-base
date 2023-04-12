'''
LC71, Medium, frequency=
'''
class SimplifyPath:
    def __init__(self):
        pass

    def simplifyPath(self, path: str) -> str:
        stack = []
        arr = path.split('/')
        for x in arr:
            if '..' == x:
                if stack:
                    stack.pop()
            elif '' != x and '.' != x and '..' != x:
                stack.append(x)
        res = '/'.join(stack)
        return '/' + res

instance = SimplifyPath()
#s = "/../"
s = "/home//foo/"
res = instance.simplifyPath(s)
print(res)