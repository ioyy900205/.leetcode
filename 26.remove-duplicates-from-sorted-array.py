# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
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
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for fast in range(len(nums)-1):
            if nums[fast] != nums[fast+1]:
                nums[slow] = nums[fast+1]
                slow += 1
        return(slow)

        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,2]')
    print('Exception :')
    print('2, nums = [1,2,_]')
    print('Output :')
    print(str(Solution().removeDuplicates([1,1,2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [0,0,1,1,1,2,2,3,3,4]')
    print('Exception :')
    print('5, nums = [0,1,2,3,4,_,_,_,_,_]')
    print('Output :')
    print(str(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])))
    print()
    
    pass
# @lc main=end