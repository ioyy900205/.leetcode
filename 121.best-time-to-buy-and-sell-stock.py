# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc tags=array;dynamic-programming

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
    def maxProfit(self, prices: List[int]) -> int:
        table = [0] * len(prices)
        min_num = prices[0]

        for i in range(1,len(prices)):
            table[i] = max(table[i-1], prices[i] - min_num)
            min_num = min(min_num, prices[i])
        return max(table)
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('prices = [7,1,5,3,6,4]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().maxProfit([7,1,5,3,6,4])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('prices = [7,6,4,3,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().maxProfit([7,6,4,3,1])))
    print()
    
    pass
# @lc main=end