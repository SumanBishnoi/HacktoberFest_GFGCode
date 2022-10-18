# Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000
S="DMC"
d={'I':'1','V': '5','X':'10', 'L': '50', 'C': '100' ,'D': '500','M': '1000'}
sum='0'
sum2=0
for s in S:
    sum=sum+'.'+d[s]
x=sum.split('.')
print(x)
for i in range(0,len(x)):
    if i!=len(x)-1:
        if int(x[i])<int(x[i+1]):
            sum2=sum2+int(x[i+1])-int(x[i])
            print(int(x[i+1]))
            i=i+2
        else:
        	sum2=sum2+int(x[i])
    else:
        sum2=sum2+int(x[i])
print(sum2)
        
