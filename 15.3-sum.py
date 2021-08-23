# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
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
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        tmp = set()
        for i in range(n-2):
            
            l = i + 1
            r = n - 1
            while l < r:
                if (nums[i] + nums[l] + nums[r]) == 0:
                    tmp.add((nums[i],nums[l],nums[r]))
                    l += 1                    
                elif (nums[i] + nums[l] + nums[r]) > 0:
                    r -= 1
                else:
                    l += 1
        # for element in tmp:
        #     res.append(element)

        return tmp
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-1,0,1,2,-1,-4]')
    print('Exception :')
    print('[[-1,-1,2],[-1,0,1]]')
    print('Output :')
    print(str(Solution().threeSum([-1,0,1,2,-1,-4])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().threeSum([])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().threeSum([0])))
    print()
    
    pass
# @lc main=end