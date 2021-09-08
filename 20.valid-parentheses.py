# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc tags=string;stack

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
    def isValid(self, s: str) -> bool:
        while len(s)>0:
            l = len(s)
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
            if l == len(s):
                return False
        return True
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "()"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValid("()")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "()[]{}"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValid("()[]{}")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "(]"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValid("(]")))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = "([)]"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValid("([)]")))
    print()
    
    print('Example 5:')
    print('Input : ')
    print('s = "{[]}"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isValid("{[]}")))
    print()
    
    pass
# @lc main=end