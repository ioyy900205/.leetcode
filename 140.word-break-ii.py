# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#


# @lc tags=dynamic-programming;backtracking

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
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]')
    print('Exception :')
    print('["cats and dog","cat sand dog"]')
    print('Output :')
    print(str(Solution().wordBreak("catsanddog",["cat","cats","and","sand","dog"])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "pineapplepenapple", wordDict =["apple","pen","applepen","pine","pineapple"]')
    print('Exception :')
    print('["pine apple pen apple","pineapple pen apple","pine applepen apple"]')
    print('Output :')
    print(str(Solution().wordBreak("pineapplepenapple",["apple","pen","applepen","pine","pineapple"])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().wordBreak("catsandog",["cats","dog","sand","and","cat"])))
    print()
    
    pass
# @lc main=end