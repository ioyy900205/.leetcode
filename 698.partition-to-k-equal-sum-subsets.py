# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#


# @lc tags=dynamic-programming;recursion

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
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, m = divmod(sum(nums), k)
        if m: return False
        dp, n = [0]*k, len(nums)
        nums.sort(reverse=True)
        i = 0
        if nums[0] > target: return False


        while i<=len(nums)-1 and nums[i]==target:
            i += 1
            k -= 1
        
        return partition(nums[k+1:], )



        return True
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,3,2,3,5,2,1], k = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canPartitionKSubsets([4,3,2,3,5,2,1],4)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4], k = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canPartitionKSubsets([1,2,3,4],3)))
    print()
    
    pass
# @lc main=end