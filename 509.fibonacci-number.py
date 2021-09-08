# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# @lc tags=tree

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
    global find_table
    find_table = {}

    def fib(self, n: int) -> int:
        if n in  find_table:
            return find_table[n]
     
        if n <= 1:
            return n
        
        result = self.fib(n-1) + self.fib(n-2)
        if n not in find_table:
            find_table[n] = result
        return result

        

        
        
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().fib(4)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().fib(3)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('n = 4')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().fib(4)))
    print()
    
    pass
# @lc main=end