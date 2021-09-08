# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc tags=backtracking

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
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums, [], result)
        return result

    def dfs(self, nums, path, result: List[int]):
        if not nums:
            result.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)




        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]')
    print('Output :')
    print(str(Solution().permute([1,2,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [0,1]')
    print('Exception :')
    print('[[0,1],[1,0]]')
    print('Output :')
    print(str(Solution().permute([0,1])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums = [1]')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().permute([1])))
    print()
    
    pass
# @lc main=end