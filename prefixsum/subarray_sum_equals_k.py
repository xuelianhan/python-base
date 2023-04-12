from typing import List

'''
LC560, Medium
'''
class SubarraySumEqualsK:
    def __init__(self):
        pass

    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        res = 0
        dict = {0:1}
        for x in nums:
            sum += x
            if sum - k in dict:
                res += dict[sum - k]
            if sum not in dict:
                dict[sum] = 1
            else:
                dict[sum] += 1
        return res

instance = SubarraySumEqualsK()
nums = [1, 2, 3]
k = 3
res = instance.subarraySum(nums, k)
print(res)