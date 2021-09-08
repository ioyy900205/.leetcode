'''
Date: 2021-09-07 09:39:54
LastEditors: Liuliang
LastEditTime: 2021-09-07 09:39:55
Description: 
'''
a = '123'
b = '456'
c = '789'

m = [i+j+k for i in a for j in b for k in c]
print(m)

