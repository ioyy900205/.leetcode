# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#


# @lc tags=tree

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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
    print('Exception :')
    print('[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]')
    print('Output :')
    print(str(Solution().convertBST([4,1,6,0,2,5,7,null,null,null,3,null,null,null,8])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [0,null,1]')
    print('Exception :')
    print('[1,null,1]')
    print('Output :')
    print(str(Solution().convertBST([0,null,1])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = [1,0,2]')
    print('Exception :')
    print('[3,3,2]')
    print('Output :')
    print(str(Solution().convertBST([1,0,2])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('root = [3,2,4,1]')
    print('Exception :')
    print('[7,9,4,10]')
    print('Output :')
    print(str(Solution().convertBST([3,2,4,1])))
    print()
    
    pass
# @lc main=end