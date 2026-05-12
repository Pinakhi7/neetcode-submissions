class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0:
                if nums[i]==nums[i-1]:
                    continue
            left = i+1
            right = len(nums)-1
            while left<right:
                current_sum = nums[i]+nums[left]+nums[right]
                if current_sum == 0:
                    a=[nums[i],nums[left],nums[right]]
                    l.append(a)
                    while left<right and nums[left]==nums[left+1]:
                        left +=1
                    left +=1
                    while left<right and nums[right]==nums[right-1]:
                        right -=1
                    right -=1
                elif current_sum>0:
                    right -=1
                else:
                    left +=1
        return l