'''
LC1268, Medium
You are given an array of strings products and a string searchWord.
Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.
Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will always be suggested while typing the search word.

Constraints:
1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 10^4
All the strings of products are unique.
products[i] consists of lowercase English letters.
1 <= searchWord.length <= 1000
searchWord consists of lowercase English letters.
'''
from typing import List

class TrieNode:
    def __init__(self):
        self.children: List[TrieNode | None] = [None] * 26
        self.idxList: List[int] = []

    def insert(self, word, i):
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
            if len(node.idxList) < 3:
                node.idxList.append(i)

    def search(self, search_word):
        node = self
        res = [[] for _ in range(len(search_word))]
        for i, c in enumerate(search_word):
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                break
            node = node.children[idx]
            res[i] = node.idxList
        return res

class SearchSuggestionsSystem:
    def suggestedProducts(self, products: List[str], search_word: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()
        for i, word in enumerate(products):
            root.insert(word, i)
        return [[products[i] for i in idxList] for idxList in root.search(search_word)]



