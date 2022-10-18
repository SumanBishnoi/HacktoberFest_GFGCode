x = int(input("Enter the no."))
sum =0
i = x

while x>=1 :

    r = x%10
    print(r)
    sum = sum + r**3
    print(sum)
    x = x//10
    print(x)


if(i==sum):
    print("no. is amstrong")
else:
    print("not amstrong")