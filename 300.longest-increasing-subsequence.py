# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc tags=binary-search;dynamic-programming

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
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [ for x in range(len(nums))]
        size = 0
        
            
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [10,9,2,5,3,7,101,18]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().lengthOfLIS([10,9,2,5,3,7,101,18])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [0,1,0,3,2,3]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().lengthOfLIS([0,1,0,3,2,3])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [7,7,7,7,7,7,7]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lengthOfLIS([7,7,7,7,7,7,7])))
    print()
    
    pass
# @lc main=end