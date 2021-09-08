# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc tags=array;binary-search

# @lc imports=start
import collections
from sys import exc_info
from imports import *
# @lc imports=end

# @lc idea=start
# 
# 
# 
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        l, h = 0, rows*cols-1
        while l<=h:
            mid = (l+h) // 2
            num = matrix[mid//cols][mid%cols]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                h = mid - 1
        return False
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13)))
    print()
    
    pass
# @lc main=end