# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#


# @lc tags=array

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
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('[1,3,2]')
    print('Output :')
    print(str(Solution().nextPermutation([1,2,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,1]')
    print('Exception :')
    print('[1,2,3]')
    print('Output :')
    print(str(Solution().nextPermutation([3,2,1])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1,1,5]')
    print('Exception :')
    print('[1,5,1]')
    print('Output :')
    print(str(Solution().nextPermutation([1,1,5])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().nextPermutation([1])))
    print()
    
    pass
# @lc main=end