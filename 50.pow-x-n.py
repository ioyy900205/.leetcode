# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#


# @lc tags=math;binary-search

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
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x,-n)
        if n%2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
 
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 2.00000, n = 10')
    print('Exception :')
    print('1024.00000')
    print('Output :')
    print(str(Solution().myPow(2.00000,10)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('x = 2.10000, n = 3')
    print('Exception :')
    print('9.26100')
    print('Output :')
    print(str(Solution().myPow(2.10000,3)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('x = 2.00000, n = -2')
    print('Exception :')
    print('0.25000')
    print('Output :')
    print(str(Solution().myPow(2.00000,-2)))
    print()
    
    pass
# @lc main=end