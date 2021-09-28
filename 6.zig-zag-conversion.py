# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#


# @lc tags=string

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
    def convert(self, s: str, numRows: int) -> str:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "PAYPALISHIRING", numRows = 3')
    print('Exception :')
    print('"PAHNAPLSIIGYIR"')
    print('Output :')
    print(str(Solution().convert("PAYPALISHIRING",3)))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "PAYPALISHIRING", numRows = 4')
    print('Exception :')
    print('"PINALSIGYAHRPI"')
    print('Output :')
    print(str(Solution().convert("PAYPALISHIRING",4)))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "A", numRows = 1')
    print('Exception :')
    print('"A"')
    print('Output :')
    print(str(Solution().convert("A",1)))
    print()
    
    pass
# @lc main=end