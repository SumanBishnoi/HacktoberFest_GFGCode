from zmq import NULL


t = int(input())
ls=[]

lenght=0
for _ in range(t):
    ls.append(int(input()))
'''for i in range(t-1):
    count = 1
    pd = -1
    for j in range(i+1,t):
        d = ls[j]-ls[j-1]
        if(pd == d):
            count=count+1
        else:
            count=1
        pd =d
        lenght=max(count,lenght)

print(lenght)'''
pd = NULL
counts=1
for i in range(t-1):
    d = ls[i+1] - ls[i]
    if (pd==d):
        counts=counts+1
    else:
        counts = 1
    pd = d
    lenght = max(lenght,counts)
print(lenght+1)