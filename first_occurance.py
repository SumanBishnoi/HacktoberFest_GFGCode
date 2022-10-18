t = int(input())
ls = []
small_ind = 10000000
store_index = [-1]*100
for _ in range(t):
    ls.append(int(input()))
for i in range(t):
    if (store_index[ls[i]]==-1):
        store_index[ls[i]]=i
    else:
        if(small_ind>store_index[ls[i]]):
            small_ind = store_index[ls[i]]
print(small_ind)