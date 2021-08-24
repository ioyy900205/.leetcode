# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#


# @lc tags=array;binary-search

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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def binarySearch(nums, target):
            low, high = 0, len(nums)-1            
            while low < high:
                mid = low + (high - low) // 2
                if target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        return [binarySearch(nums,target), binarySearch(nums,target+1)-1]

        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [5,7,7,8,8,10], target = 8')
    print('Exception :')
    print('[3,4]')
    print('Output :')
    print(str(Solution().searchRange([5,7,7,8,8,10],8)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [5,7,7,8,8,10], target = 6')
    print('Exception :')
    print('[-1,-1]')
    print('Output :')
    print(str(Solution().searchRange([5,7,7,8,8,10],6)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [], target = 0')
    print('Exception :')
    print('[-1,-1]')
    print('Output :')
    print(str(Solution().searchRange([],0)))
    print()
    
    pass
# @lc main=end