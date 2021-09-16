# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,3,4,5]')
    print('Exception :')
    print('[5,4,3,2,1]')
    print('Output :')
    print(str(Solution().reverseList([1,2,3,4,5])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [1,2]')
    print('Exception :')
    print('[2,1]')
    print('Output :')
    print(str(Solution().reverseList([1,2])))
    print()
    
    print('Example 3:')
    print('Input : ')
    print('head = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().reverseList([])))
    print()
    
    pass
# @lc main=end