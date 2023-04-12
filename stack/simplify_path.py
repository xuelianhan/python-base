'''
LC71, Medium, frequency=
'''
class SimplifyPath:
    def __init__(self):
        pass

    def simplifyPathV1(self, path: str) -> str:
        stack = []
        for x in path.split('/'):
            if '..' == x and stack:
                stack.pop()
            elif x not in ['', '.', '..']:
                stack.append(x)
        return '/' + '/'.join(stack)

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