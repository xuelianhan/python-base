import collections
from typing import List

"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
LC1207

"""


class UniqueNumbeOfOccurrences:
    def uniqueOccurrencesV1(self, arr: List[int]) -> bool:
        seen = set()
        for freq in collections.Counter(arr).values():
            if freq in seen:
                return False
            seen.add(freq)
        return True

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values()))


if __name__ == '__main__':
    arr = [1, 2, 2, 1, 1, 3]
    instance = UniqueNumbeOfOccurrences()
    res = instance.uniqueOccurrences(arr)
    print(res)
