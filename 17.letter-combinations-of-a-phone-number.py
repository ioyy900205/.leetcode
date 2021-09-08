# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
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
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        
        prev = self.letterCombinations(digits[:-1])
        addition = mapping[digits[-1]]
        return [s+c for s in prev for c in addition]
        
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('digits = "23"')
    print('Exception :')
    print('["ad","ae","af","bd","be","bf","cd","ce","cf"]')
    print('Output :')
    print(str(Solution().letterCombinations("234")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('digits = ""')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().letterCombinations("")))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('digits = "2"')
    print('Exception :')
    print('["a","b","c"]')
    print('Output :')
    print(str(Solution().letterCombinations("2")))
    print()
    
    pass
# @lc main=end