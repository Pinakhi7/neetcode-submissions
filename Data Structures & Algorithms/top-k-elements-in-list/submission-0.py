from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        l= defaultdict(list)
        top=[]
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for num,count in freq.items():
            l[count].append(num)
        for i in range(len(nums),0,-1):
            for n in l[i]:
                top.append(n)
                if len(top)==k:
                    return top