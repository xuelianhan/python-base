import collections
from typing import List


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
