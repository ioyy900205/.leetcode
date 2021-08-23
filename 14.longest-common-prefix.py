# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
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
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["flower","flow","flight"]')
    print('Exception :')
    print('"fl"')
    print('Output :')
    print(str(Solution().longestCommonPrefix(["flower","flow","flight"])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('strs = ["dog","racecar","car"]')
    print('Exception :')
    print('""')
    print('Output :')
    print(str(Solution().longestCommonPrefix(["dog","racecar","car"])))
    print()
    
    pass
# @lc main=end