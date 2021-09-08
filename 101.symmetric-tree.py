# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(L,R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root,root)


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('root = [1,2,2,3,4,4,3]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isSymmetric([1,2,2,3,4,4,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('root = [1,2,2,null,3,null,3]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isSymmetric([1,2,2,null,3,null,3])))
    print()
    
    pass
# @lc main=end