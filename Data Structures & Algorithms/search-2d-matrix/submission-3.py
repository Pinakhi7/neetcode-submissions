class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     low = 0
        #     high =len(matrix[i])-1
        #     while low<= high:
        #         if target > matrix[i][high]:
        #             break
        #         elif target == matrix[i][high]:
        #             return True
        #         elif target == matrix[i][low]:
        #             return True
        #         else:
        #             mid = (low+high)//2
        #             if target == matrix[i][mid]:
        #                 return True
        #             elif target > matrix[i][mid]:
        #                 low = mid+1
        #             else:
        #                 high = mid-1
        # return False
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])

        low = 0
        high = (row*col)-1
        while low<= high:
            mid = (low+high)//2
            mid_element = matrix[mid//col][mid%col]
            if target == mid_element:
                return True
            elif target>mid_element:
                low = mid + 1
            else:
                high = mid-1
        return False

        # for i in range(len(matrix)):
        #     low = 0
        #     high = len(matrix[i]) - 1
            
        #     # Fast skip: If the target can't possibly fit in this row, 
        #     # don't even enter the while loop. Move to the next row.
        #     if target < matrix[i][low] or target > matrix[i][high]:
        #         continue
                
        #     # Standard, bulletproof binary search
        #     while low <= high:
        #         mid = (low + high) // 2
                
        #         if matrix[i][mid] == target:
        #             return True
        #         elif matrix[i][mid] < target:
        #             low = mid + 1
        #         else:
        #             high = mid - 1
                    
        # return False