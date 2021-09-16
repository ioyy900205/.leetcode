# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root == None:
            return
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [4,2,7,1,3,6,9]')
    print('Exception :')
    print('[4,7,2,9,6,3,1]')
    print('Output :')
    print(str(Solution().invertTree([4,2,7,1,3,6,9])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [2,1,3]')
    print('Exception :')
    print('[2,3,1]')
    print('Output :')
    print(str(Solution().invertTree([2,1,3])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('root = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().invertTree([])))
    print()
    
    pass
# @lc main=end