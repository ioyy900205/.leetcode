'''
Date: 2021-08-28 09:12:42
LastEditors: Liuliang
LastEditTime: 2021-08-28 09:17:08
Description: 
'''

from typing import List



def bst(nums: List,target: int):
    if not nums:
        return None
   
    l, r = 0, len(nums)-1
    mid = l + (r - l) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        bst(nums[mid+1:r+1], target)
    else:
        bst(nums[l:mid-1], target)
    
        

nums = [1,2,3,4,5,6,7,8,9]

target = 5

print(bst(nums,target))