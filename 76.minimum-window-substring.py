# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#


# @lc tags=hash-table;two-pointers;string;sliding-window

# @lc imports=start
import collections
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
    def minWindow(self, s: str, t: str) -> str:
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
     
        for j, c in enumerate(s,1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
     
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ADOBECODEBANC", t = "ABC"')
    print('Exception :')
    print('"BANC"')
    print('Output :')
    print(str(Solution().minWindow("ADOBECODEBANC","ABC")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "a", t = "a"')
    print('Exception :')
    print('"a"')
    print('Output :')
    print(str(Solution().minWindow("a","a")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "a", t = "aa"')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().minWindow("a","aa")))
    print()
    
    pass
# @lc main=end