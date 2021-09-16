# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


# @lc tags=dynamic-programming

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
    def rob(self, nums: List[int]) -> int:
        table = [0] * len(nums)
        for i, element in enumerate(nums):
            if i == 0:
                table[i] = nums[0]
            if i == 1:
                table[i] = nums[1]

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,1]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().rob([1,2,3,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [2,7,9,3,1]')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().rob([2,7,9,3,1])))
    print()
    
    pass
# @lc main=end