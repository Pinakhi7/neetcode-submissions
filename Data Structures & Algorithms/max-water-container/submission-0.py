class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights)-1
        left = 0 
        max_area =0
        while left<right:
            width = right-left
            effective_height = min(heights[right],heights[left])
            area = width*effective_height
            max_area = max(area,max_area)
            if heights[left]<heights[right]:
                left +=1
            else:
                right -=1
        return max_area
