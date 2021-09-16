# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#


# @lc tags=linked-list;two-pointers

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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True
        fast = head
        slow = head
        while(fast.next!=None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next
        new_head = self.reverse(slow.next)
        while(new_head != None):
            if(head.val != new_head.val):
                return False
            head = head.next
            new_head = new_head.next
        return True

    def reverse(self, head):
        if head.next == None:
            return head
        pre = None
        while(head != None):
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre


        pass
        
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('head = [1,2,2,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isPalindrome([1,2,2,1])))
    print()
    
    print('Example 2:')
    print('Input : ')
    print('head = [1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isPalindrome([1,2])))
    print()
    
    pass
# @lc main=end