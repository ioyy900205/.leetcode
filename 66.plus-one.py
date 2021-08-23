# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc tags=array

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
    def plusOne(self, digits: List[int]) -> List[int]:
        plusone = 1        
        for i in range(len(digits)-1,-1,-1):    
            tmp = (digits[i] + plusone) // 10
            digits[i] = (digits[i] + plusone) % 10 
            plusone = tmp
            
        if plusone:
            return [1] + digits 
        return digits
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('digits = [1,2,3]')
    print('Exception :')
    print('[1,2,4]')
    print('Output :')
    print(str(Solution().plusOne([1,2,3])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('digits = [4,3,2,1]')
    print('Exception :')
    print('[4,3,2,2]')
    print('Output :')
    print(str(Solution().plusOne([4,3,2,1])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('digits = [0]')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().plusOne([0])))
    print()
    
    pass
# @lc main=end