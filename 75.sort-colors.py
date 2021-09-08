# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#


# @lc tags=array;two-pointers;sort

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
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,0,2,1,1,0]')
    print('Exception :')
    print('[0,0,1,1,2,2]')
    print('Output :')
    print(str(Solution().sortColors([2,0,2,1,1,0])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [2,0,1]')
    print('Exception :')
    print('[0,1,2]')
    print('Output :')
    print(str(Solution().sortColors([2,0,1])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().sortColors([0])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().sortColors([1])))
    print()
    
    pass
# @lc main=end