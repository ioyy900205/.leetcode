# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#


# @lc tags=string;backtracking

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
    def generateParenthesis(self, n: int) -> List[str]:
        def generate_parenthesis(p,left,right,parent=[]):
            if left:
                generate_parenthesis(p+'(',left-1,right)
            if right>left:
                generate_parenthesis(p+')',left,right-1)
            if not right:
                parent.append(p)
            return parent
        return generate_parenthesis('',n,n)
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('["((()))","(()())","(())()","()(())","()()()"]')
    print('Output :')
    print(str(Solution().generateParenthesis(3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('["()"]')
    print('Output :')
    print(str(Solution().generateParenthesis(1)))
    print()
    
    pass
# @lc main=end