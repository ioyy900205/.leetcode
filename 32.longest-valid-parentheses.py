# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#


# @lc tags=string;dynamic-programming

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
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for x in range(len(s))]
        max_to_now = 0
        # dp records the longestvalidparenthese
        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                else:
                    dp[i] = 0
                max_to_now = max(max_to_now,dp[i])
        return max_to_now
            

                        
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "(()"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().longestValidParentheses("(()())")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = ")()())"')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().longestValidParentheses(")()())")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = ""')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().longestValidParentheses("")))
    print()
    
    pass
# @lc main=end