'''
Date: 2021-09-03 16:29:44
LastEditors: Liuliang
LastEditTime: 2021-09-03 16:40:42
Description: 
'''

def backtracking(n, i, track):
    if i == 2*n:
        print(track)
        return

    for choice in ['1','2']:
        track.append(choice)
        backtracking(n,i+1,track)
        track.pop()

backtracking(1,0,[])
