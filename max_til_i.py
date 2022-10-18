from ctypes.wintypes import PINT


t= int(input())
li=[]
max_till = []
for _ in range(t):
    li.append(int(input()))
max_no = li[0]
for i in range(1,t):
    if(max_no>=li[i]):
        max_till.append(max_no)
    else:
        max_no = li[i]
        max_till.append(max_no)
for i in range(t-1):
    print(max_till[i])