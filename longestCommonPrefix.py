
strs = ["dog","racecar","car"]

condition = True
minLenght = min([len(i) for i in strs])
ls=[]
j=0
while(j<minLenght):
    temp = strs[0][j]
    for i in range(len(strs)):
        if(temp==strs[i][j]):
            temp=strs[i][j]
        else:
            break
    if(i==len(strs)-1 and temp == strs[i][j]):
        ls.append(temp)
        j=j+1
    else:
        break
print("".join(ls))