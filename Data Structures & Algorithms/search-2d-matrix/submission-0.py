class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            low = 0
            high =len(matrix[i])-1
            while low<= high:
                if target > matrix[i][high]:
                    break
                elif target == matrix[i][high]:
                    return True
                elif target == matrix[i][low]:
                    return True
                else:
                    mid = (low+high)//2
                    if target == matrix[i][mid]:
                        return True
                    elif target > matrix[i][mid]:
                        low = mid+1
                    else:
                        high = mid-1
        return False