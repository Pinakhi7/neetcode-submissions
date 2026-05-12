class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers = set(numbers)
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-indexed positions
                return [left + 1, right + 1]
            
            if current_sum < target:
                # Sum is too small, need a bigger number (move left)
                left += 1
            else:
                # Sum is too big, need a smaller number (move right)
                right -= 1