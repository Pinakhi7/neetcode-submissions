class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_v = 0
        
        while l < r:
            # Calculate only when we find a potentially better height
            h_l, h_r = height[l], height[r]
            h = h_l if h_l < h_r else h_r
            
            current_area = h * (r - l)
            if current_area > max_v:
                max_v = current_area
            
            # Skip pointers that are shorter than the current bottleneck
            if h_l < h_r:
                while l < r and height[l] <= h_l:
                    l += 1
            else:
                while l < r and height[r] <= h_r:
                    r -= 1
                    
        return max_v