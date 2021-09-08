# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc tags=linked-list;math

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
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('l1 = [2,4,3], l2 = [5,6,4]')
    print('Exception :')
    print('[7,0,8]')
    print('Output :')
    print(str(Solution().addTwoNumbers([2,4,3],[5,6,4])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('l1 = [0], l2 = [0]')
    print('Exception :')
    print('[0]')
    print('Output :')
    print(str(Solution().addTwoNumbers([0],[0])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]')
    print('Exception :')
    print('[8,9,9,9,0,0,0,1]')
    print('Output :')
    print(str(Solution().addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])))
    print()
    
    pass
# @lc main=end