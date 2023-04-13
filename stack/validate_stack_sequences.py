from typing import List

'''
LC946
'''

class ValidateStackSequences:
    def __init__(self):
        pass

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:
            stack.append(x)
            while stack and stack[len(stack) - 1] == popped[j]:
                stack.pop()
                j+=1
        return len(stack) == 0

instance = ValidateStackSequences()
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
res = instance.validateStackSequences(pushed, popped)
print(res)