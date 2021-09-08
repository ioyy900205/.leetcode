# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc tags=array;two-pointers;binary-search

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
    def findDuplicate(self, nums: List[int]) -> int:
        p = q = 0
        while True:
            p = nums[p]
            q = nums[nums[q]]
            if p == q:
                break
        q = 0
        while p != q:
            p = nums[p]
            q = nums[q]
        return p
        
        
        


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,4,2,2]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findDuplicate([1,3,4,2,2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [3,1,3,4,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findDuplicate([3,1,3,4,2])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findDuplicate([1,1])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('nums = [1,1,2]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().findDuplicate([1,1,2])))
    print()
    
    pass
# @lc main=end