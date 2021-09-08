# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#


# @lc tags=string;dynamic-programming;backtracking

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
    def isMatch(self, s: str, p: str) -> bool:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aa", p = "a"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isMatch("aa","a")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "aa", p = "a*"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isMatch("aa","a*")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "ab", p = ".*"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isMatch("ab",".*")))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = "aab", p = "c*a*b"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isMatch("aab","c*a*b")))
    print()
    
    print('Example 5:')
    print('Input : ')
    print('s = "mississippi", p = "mis*is*p*."')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isMatch("mississippi","mis*is*p*.")))
    print()
    
    pass
# @lc main=end