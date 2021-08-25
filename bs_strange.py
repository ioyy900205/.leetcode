'''
Date: 2021-08-24 10:15:12
LastEditors: Liuliang
LastEditTime: 2021-08-24 10:18:13
Description: 
'''
# from _typeshed import HasFileno


def bs(nums,target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif mid == 0 or nums[mid-1] != nums[mid]:
            return mid
        else:
            right = mid - 1
    return left

nums = [1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4]

print(bs(nums,2))