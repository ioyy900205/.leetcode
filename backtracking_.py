'''
Date: 2021-09-27 15:38:07
LastEditors: Liuliang
LastEditTime: 2021-09-28 11:53:50
Description: 
'''
nums = [1,2,3]

n = len(nums)
res = []
state = []
used = [False] * n

global cnt
cnt = 0

def dfs_backtrack(depth = 0):
    global cnt
    cnt += 1
    if depth == n:        
        res.append(state[:])
        return

    for i in range(n):
        
        if used[i]:
            continue
        state.append(nums[i])
        used[i] = True
        
        dfs_backtrack(depth=depth+1)
        print(state)        
        state.pop()
        used[i] = False

    return res

c = dfs_backtrack()

print(c)
print(cnt)
