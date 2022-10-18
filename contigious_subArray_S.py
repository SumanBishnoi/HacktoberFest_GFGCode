t = int(input()) ### size of array
s = int(input()) ### sum value
ls = []
for _ in range(t):
    ls.append(int(input()))
i=0
j=0
sum=0
while (j<t):
    sum = sum + ls[j]
    if (sum == s):
        print(i+1," ",j+1)
        break
    elif(sum>s):
        while(sum>=s):
            sum = sum-ls[i]
            if(sum==s):
                print(i+1," ",j+1)
                break
            else:
                i=i+1
        j=j+1
    else:
        j=j+1