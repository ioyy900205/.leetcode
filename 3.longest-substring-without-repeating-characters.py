# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc tags=hash-table;two-pointers;string;sliding-window

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
    def lengthOfLongestSubstring(self, s: str) -> int:

        lenth = len(s)
        i = 0
        table = {}
        result = 0

        for j, char in enumerate(s):
            if char in table and i <= table[char]:
                i = table[char] + 1
            else:                
                result = max(result, j-i+1)
            table[char] = j

        return result
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "tmmzuxt"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("bbtablud")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "bbbbb"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("bbbbb")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "pwwkew"')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("pwwkew")))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('s = ""')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().lengthOfLongestSubstring("")))
    print()
    
    pass
# @lc main=end
