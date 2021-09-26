# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
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
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        subarray_min = inf
        subarray_max = -inf

        while left < right and nums[left] <= nums[left+1]:
            left += 1
        if left == right:
            return 0

        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1
        
        for i in range(left, right+1):
            subarray_min = min(subarray_min, nums[i])
            subarray_max = max(subarray_max, nums[i])

        while left > 0 and nums[left-1] > subarray_min:
            left -= 1
        
        while right < len(nums)-1 and nums[right+1] < subarray_max:
            right += 1

        return right - left + 1
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,6,4,8,10,9,15]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findUnsortedSubarray([2,6,4,8,10,9,15])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findUnsortedSubarray([1,2,3,4])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findUnsortedSubarray([1])))
    print()
    
    pass
# @lc main=end
