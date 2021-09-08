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
    def findMedianSortedArrays(self, A, B):
        lenth_1, lenth_2 = len(A), len(B)
        if lenth_1 == lenth_2 == 0: return

        if lenth_1 > lenth_2:
            A, B = B, A
            lenth_1, lenth_2 = len(A), len(B)
        
        half = (lenth_1 + lenth_2 + 1) // 2
        even = True if (lenth_1 + lenth_2)%2 == 0 else False

        start, end = 0, lenth_1
        apart = bpart = 0
        
        while start <= end:
            apart = (start+end) // 2
            bpart = half - apart
            if apart>start and A[apart-1] > B[bpart]:
                end = apart - 1
            elif apart<end and A[apart] < B[bpart-1]:
                start = apart + 1
            else:
                leftmax = 0
                if apart == 0:
                    leftmax = B[bpart-1]
                elif bpart == 0:
                    leftmax = A[apart-1]
                else:
                    leftmax = max(A[apart-1],B[bpart-1])
                
                if not even:
                    return leftmax

                rightmin = 0
                if apart == lenth_1:
                    rightmin = B[bpart]
                elif bpart == lenth_2:
                    rightmin = A[apart]
                else:
                    rightmin = min(A[apart], B[bpart])
                return (leftmax + rightmin) / 2
                
                
        
   
        
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
    print(str(Solution().findMedianSortedArrays([1,2,3,4,5],[3,4,5,6,7,8])))
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