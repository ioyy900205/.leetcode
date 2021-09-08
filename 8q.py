'''
Date: 2021-08-26 12:12:32
LastEditors: Liuliang
LastEditTime: 2021-08-26 15:05:02
Description: 
'''
result = []

def cal(row):
    if row == 8:
        printQ(result)
        return
    for column in range(row):
        if isOk(row,column):
            result[row] = column
            cal(row + 1)

def printQ(result):
    for row in range(8):
        for column in range(8):
            if result[row] == column:
                print('Q ')
            else:
                print('*')
            print('/n')

        print('/n')
    

def isOk(row,column):
    leftup, rightup = column-1, column+1
    for i in range(row-1, -1, -1):
        if result[i] == column: 
            return False
        if leftup >= 0 and result[i] == leftup:
            return False
        if rightup <= 8 and result[i] == rightup:
            return False
        leftup -= 1
        rightup += 1
    return True

cal(0)