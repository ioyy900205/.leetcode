# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc tags=array;two-pointers

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
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
        return nums

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [0,1,0,3,12]')
    print('Exception :')
    print('[1,3,12,0,0]')
    print('Output :')
    print(str(Solution().moveZeroes([0,1,0,3,12])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().moveZeroes([0])))
    print()
    
    pass
# @lc main=end