class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # 1. Check if we found the target
            if nums[mid] == target:
                return mid
            
            # 2. Determine if the Left side is normally sorted
            if nums[low] <= nums[mid]:
                # Is the target safely inside this sorted left zone?
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Search left
                else:
                    low = mid + 1   # Search right
                    
            # 3. Otherwise, the Right side must be normally sorted
            else:
                # Is the target safely inside this sorted right zone?
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Search right
                else:
                    high = mid - 1  # Search left
                    
        return -1  # Target was never found