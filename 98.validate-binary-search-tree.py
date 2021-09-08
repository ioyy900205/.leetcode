# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#


# @lc tags=tree;depth-first-search

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, low=-math.inf, high=math.inf):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            
            return (validate(root.left, low, root.val) and validate(root.right, root.val, high))

        return validate(root)
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [2,1,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValidBST([2,1,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [5,1,4,null,null,3,6]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValidBST([5,1,4,null,null,3,6])))
    print()
    
    pass
# @lc main=end