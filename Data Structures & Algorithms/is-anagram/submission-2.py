from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # count ={}
        # for char in s:
        #     count[char] = count.get(char,0)+1
        # for ch in t:
        #     if ch not in count or count[ch]==0:
        #         return False
        #     count[ch]-=1
        # return True
        return Counter(s)==Counter(t)