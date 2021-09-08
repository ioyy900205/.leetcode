'''
Date: 2021-09-08 17:56:24
LastEditors: Liuliang
LastEditTime: 2021-09-08 17:58:28
Description: 
'''

string_1 = "12343221"

def judge(stings):
    left, right = 0, len(stings)-1
    while left < right:
        if stings[left] == stings[right]:
            left += 1
            right -= 1
        else:
            return False
    return True    

print(judge(string_1))