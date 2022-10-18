t = int(input())
ls = []
for _ in range(t):
    ls.append(int(input()))
max = -1
count = 0
for i in range(t):
    if (i != t-1):
        if(max<=ls[i] and ls[i]> ls[i+1]):
            count = count +1
            max = ls[i]
        else:
            pass
    else:
        if (ls[i]>=max):
            count = count +1
        else:
            pass
print(count)

