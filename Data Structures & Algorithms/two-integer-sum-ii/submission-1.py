class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = set(numbers)
        dic = {}
        for i , n in enumerate(numbers):
            diff = target - n
            if diff in dic:
                return [dic[diff]+1,i+1]
            dic[n] = i