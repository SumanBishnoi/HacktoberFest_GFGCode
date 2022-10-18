n = int(input(""))
arr=[]
for _ in range(n):
    arr.append(int(input()))
print("---")
target = int(input())

def binary(start,end,target):
    if(start==end):
        if(arr[start]==target):
            return start
        else:
            return 0
    mid = int((start + end)/2)
    if(arr[mid]==target):
        return mid
    elif(arr[mid]>target):
        end = mid-1
        return binary(start,end,target)
    else:
        start = mid+1
        return binary(start,end,target)
print(binary(0,n-1,target))
