class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod_l=[1]*n
        pre = 1
        
        for i in range(n):
            prod_l[i] = pre
            pre *=nums[i]
        post =1
        for i in range(n-1,-1,-1):
            prod_l[i] *= post
            post *= nums[i]
        return prod_l