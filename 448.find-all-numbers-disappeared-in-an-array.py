# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
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
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                tmp = nums[i]
                nums[i] = nums[nums[i]-1] 
                nums[tmp-1] = tmp
                if nums[i] == nums[nums[i]-1]:
                    break
        result= []
        for i, val in enumerate(nums):
            if i+1 != val:
                result.append(i+1)
        return result

  

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [4,3,2,7,8,2,3,1]')
    print('Exception :')
    print('[5,6]')
    print('Output :')
    print(str(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums = [1,1]')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(str(Solution().findDisappearedNumbers([1,1])))
    print()
    
    pass
# @lc main=end