# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc tags=math

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
    def reverse(self, x: int) -> int:       
        r = int(str(abs(x))[::-1])
        s = (x>0)-(x<0)
        return r*s*(x<2**31) if -2**31<=r*s<=2**31-1 else 0

     
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 123')
    print('Exception :')
    print('321')
    print('Output :')
    print(str(Solution().reverse(123)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('x = -123')
    print('Exception :')
    print('-321')
    print('Output :')
    print(str(Solution().reverse(-123)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('x = 120')
    print('Exception :')
    print('21')
    print('Output :')
    print(str(Solution().reverse(120)))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('x = 0')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().reverse(0)))
    print()
    
    pass
# @lc main=end