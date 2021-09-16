# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc tags=array;divide-and-conquer;bit-manipulation

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
    def majorityElement(self, nums: List[int]) -> int:
        table = {}
        for n in nums:
            table[n] = table.get(n,0) + 1
            if table[n] > len(nums) // 2:
                return n
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,3]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().majorityElement([3,2,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,1,1,1,2,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().majorityElement([2,2,1,1,1,2,2])))
    print()
    
    pass
# @lc main=end