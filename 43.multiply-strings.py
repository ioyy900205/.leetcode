# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#


# @lc tags=math;string

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
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < 0 or len(num2) < 0:
            return False
        res = []
        count = -1
        for i in range(len(num1)-1,-1,-1):
            plus = 0
            str_j = ''
            count += 1
            for j in range(len(num2)-1,-1,-1):                
                tmp = int(num1[i])*int(num2[j])+plus
                plus = tmp // 10
                left = tmp % 10
                str_j = str(left) + str_j
            str_j = str(plus) + str_j +  '0'*count     
            # print(str_j)
            res.append(str_j)
        sum = 0

        for element in res:
            sum += int(element)
        return str(sum)

        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num1 = "2", num2 = "3"')
    print('Exception :')
    print('"6"')
    print('Output :')
    print(str(Solution().multiply("2","3")))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('num1 = "123", num2 = "456"')
    print('Exception :')
    print('"56088"')
    print('Output :')
    print(str(Solution().multiply("123","456")))
    print()
    
    pass
# @lc main=end