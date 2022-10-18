A=[2,-6,-8,1,4]
N=5
sum=A[0]
sml_sum=sum
for i in range(1,N):
    if sum>A[i] and sum>0:
        sum=A[i]
    else:
        sum=sum+A[i]
    sml_sum=min(sum,sml_sum)
    # print(sml_sum)
print(sml_sum)