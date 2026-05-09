class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        for i ,num in enumerate(nums):
            diff = target-num
            if diff in s:
                a =  [s[diff],i]
                return a
            s[num]=i