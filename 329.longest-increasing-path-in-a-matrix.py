# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#


# @lc tags=depth-first-search;topological-sort;memoization

# @lc imports=start
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
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matrix = [[9,9,4],[6,6,8],[2,1,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('matrix = [[3,4,5],[3,2,6],[2,2,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('matrix = [[1]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().longestIncreasingPath([[1]])))
    print()
    
    pass
# @lc main=end