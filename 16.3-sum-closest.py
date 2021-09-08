# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-1,2,1,-4], target = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().threeSumClosest([-1,2,1,-4],1)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [0,0,0], target = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().threeSumClosest([0,0,0],1)))
    print()
    
    pass
# @lc main=end