class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_l=[]
        n=len(nums)
        for i in range(n):
            if i==0:
                prod=1
                for j in (nums[i+1:]):
                    prod*=j
                prod_l.append(prod)
            elif i == n-1:
                prod_b=1
                for j in (nums[:n-1]):
                    prod_b*=j
                prod_l.append(prod_b)
            else:
                prod_d = 1 
                for j in nums[:i]:
                    prod_d*=j
                for j in nums[i+1:]:
                    prod_d*=j
                prod_l.append(prod_d)
        return prod_l

                
