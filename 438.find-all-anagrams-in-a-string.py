# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#


# @lc tags=hash-table

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
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = sorted(p)
        lenth = len(p)
        result = []
        for i in range(len(s)-len(p)+1):
            compare = sorted(s[i:i+len(p)])
            if target == compare:
                result.append(i)
        return result
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "cbaebabacd", p = "abc"')
    print('Exception :')
    print('[0,6]')
    print('Output :')
    print(str(Solution().findAnagrams("cbaebabacd","abc")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "abab", p = "ab"')
    print('Exception :')
    print('[0,1,2]')
    print('Output :')
    print(str(Solution().findAnagrams("abab","ab")))
    print()
    
    pass
# @lc main=end