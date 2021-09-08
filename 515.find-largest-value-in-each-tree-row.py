# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#


# @lc tags=tree;depth-first-search;breadth-first-search

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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,3,2,5,3,null,9]')
    print('Exception :')
    print('[1,3,9]')
    print('Output :')
    print(str(Solution().largestValues([1,3,2,5,3,null,9])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1,2,3]')
    print('Exception :')
    print('[1,3]')
    print('Output :')
    print(str(Solution().largestValues([1,2,3])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().largestValues([1])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('root = [1,null,2]')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().largestValues([1,null,2])))
    print()
    
    print('Example 5:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().largestValues([])))
    print()
    
    pass
# @lc main=end