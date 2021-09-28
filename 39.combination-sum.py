# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc tags=array;backtracking

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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        pass

    def calculate(self, candidates, target):
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('candidates = [2,3,6,7], target = 7')
    print('Exception :')
    print('[[2,2,3],[7]]')
    print('Output :')
    print(str(Solution().combinationSum([2,3,6,7],7)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('candidates = [2,3,5], target = 8')
    print('Exception :')
    print('[[2,2,2,2],[2,3,3],[3,5]]')
    print('Output :')
    print(str(Solution().combinationSum([2,3,5],8)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('candidates = [2], target = 1')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().combinationSum([2],1)))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('candidates = [1], target = 1')
    print('Exception :')
    print('[[1]]')
    print('Output :')
    print(str(Solution().combinationSum([1],1)))
    print()
    
    print('Example 5:')
    print('Input : ')
    print('candidates = [1], target = 2')
    print('Exception :')
    print('[[1,1]]')
    print('Output :')
    print(str(Solution().combinationSum([1],2)))
    print()
    
    pass
# @lc main=end