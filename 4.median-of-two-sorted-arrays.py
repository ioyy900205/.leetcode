# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc tags=array;binary-search;divide-and-conquer

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
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j = 0,0
        lenth = len(nums1) + len(nums2)
        count = 0
        output = []
        while i+j <= lenth // 2:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] > nums2[j]:
                    output.append(nums2[j])
                    j += 1
                else:
                    output.append(nums1[i])
                    i += 1  
            elif j<len(nums2):
                output.append(nums2[j])
                j += 1
            else:
                output.append(nums1[i])
                i += 1 
        if lenth % 2 == 1:                          
            return output[-1]        
        else:
            return ((output[-1]+output[-2]) / 2)
        
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,3], nums2 = [2]')
    print('Exception :')
    print('2.00000')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([1,3],[2])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('nums1 = [1,2], nums2 = [3,4]')
    print('Exception :')
    print('2.50000')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([1,2],[3,4])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('nums1 = [0,0], nums2 = [0,0]')
    print('Exception :')
    print('0.00000')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([0,0],[0,0])))
    print()
    
    print('Example 4:')
    print('Input : ')
    print('nums1 = [], nums2 = [1]')
    print('Exception :')
    print('1.00000')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([],[1])))
    print()
    
    print('Example 5:')
    print('Input : ')
    print('nums1 = [2], nums2 = []')
    print('Exception :')
    print('2.00000')
    print('Output :')
    print(str(Solution().findMedianSortedArrays([2],[])))
    print()
    
    pass
# @lc main=end