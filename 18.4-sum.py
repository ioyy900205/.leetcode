# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#


# @lc tags=array;hash-table;two-pointers

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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.findNsum(nums,target,4,[],results)
        return results

    def findNsum(self, nums, target, N, result, results):
        
        if N == 2:
            l,r = 0,len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])                    
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):
                if target < nums[i]*N or target > nums[-1]*N:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        
        return
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [5,5,3,5,1,-5,1,-2], target = 4')
    print('Exception :')
    print('[[-5,1,3,5]]')
    print('Output :')
    print(str(Solution().fourSum([5,5,3,5,1,-5,1,-2],4)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [2,2,2,2,2], target = 8')
    print('Exception :')
    print('[[2,2,2,2]]')
    print('Output :')
    print(str(Solution().fourSum([2,2,2,2,2],8)))
    print()
    
    pass
# @lc main=end