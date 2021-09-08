# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc tags=array;sort

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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('intervals = [[1,3],[6,9]], newInterval = [2,5]')
    print('Exception :')
    print('[[1,5],[6,9]]')
    print('Output :')
    print(str(Solution().insert([[1,3],[6,9]],[2,5])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]')
    print('Exception :')
    print('[[1,2],[3,10],[12,16]]')
    print('Output :')
    print(str(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('intervals = [], newInterval = [5,7]')
    print('Exception :')
    print('[[5,7]]')
    print('Output :')
    print(str(Solution().insert([],[5,7])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('intervals = [[1,5]], newInterval = [2,3]')
    print('Exception :')
    print('[[1,5]]')
    print('Output :')
    print(str(Solution().insert([[1,5]],[2,3])))
    print()
    
    print('Example 5:')
    print('Input : ')
    print('intervals = [[1,5]], newInterval = [2,7]')
    print('Exception :')
    print('[[1,7]]')
    print('Output :')
    print(str(Solution().insert([[1,5]],[2,7])))
    print()
    
    pass
# @lc main=end