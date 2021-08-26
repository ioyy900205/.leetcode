# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
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
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "25525511135"')
    print('Exception :')
    print('["255.255.11.135","255.255.111.35"]')
    print('Output :')
    print(str(Solution().restoreIpAddresses("25525511135")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "0000"')
    print('Exception :')
    print('["0.0.0.0"]')
    print('Output :')
    print(str(Solution().restoreIpAddresses("0000")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "1111"')
    print('Exception :')
    print('["1.1.1.1"]')
    print('Output :')
    print(str(Solution().restoreIpAddresses("1111")))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = "010010"')
    print('Exception :')
    print('["0.10.0.10","0.100.1.0"]')
    print('Output :')
    print(str(Solution().restoreIpAddresses("010010")))
    print()
    
    print('Example 5:')
    print('Input : ')
    print('s = "101023"')
    print('Exception :')
    print('["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]')
    print('Output :')
    print(str(Solution().restoreIpAddresses("101023")))
    print()
    
    pass
# @lc main=end