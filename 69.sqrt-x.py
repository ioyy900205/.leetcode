# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
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
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            elif mid * mid < x and (mid + 1) * (mid + 1) > x:
                return mid
            else:
                l = mid + 1
        return False

# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('x = 4')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().mySqrt(4)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('x = 8')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().mySqrt(8)))
    print()
    
    pass
# @lc main=end