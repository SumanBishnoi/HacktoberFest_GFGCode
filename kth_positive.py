n=int(input("Enter size"))
arr=[]
for _ in range(n):
    arr.append(int(input("")))


k=int(input())

def kthMissingNo(arr,k):
    if arr[n-1]-(n-1)==0:
        return arr[n-1]+k
    elif arr[0]>k:
        return k
    else:
        start=0
        end = len(arr)
        while(start<=end):
            mid=(start+end)/2
            if(arr[mid]-(mid+1)<=k):
                start=mid +1    
            else:
                end=mid-1
        return start+k
print(kthMissingNo(arr,k))