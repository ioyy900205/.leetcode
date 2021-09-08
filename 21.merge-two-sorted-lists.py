# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc tags=linked-list

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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
       
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('l1 = [1,2,4], l2 = [1,3,4]')
    print('Exception :')
    print('[1,1,2,3,4,4]')
    print('Output :')
    print(str(Solution().mergeTwoLists([1,2,4],[1,3,4])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('l1 = [], l2 = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().mergeTwoLists([],[])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('l1 = [], l2 = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().mergeTwoLists([],[0])))
    print()
    
    pass
# @lc main=end