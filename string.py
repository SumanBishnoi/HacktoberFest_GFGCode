
# Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, act and tac are an anagram of each other.

a="geeksforgeeks"
b="forgeeksgeks"
ls1=[]
ls2=[]
ls1=sorted(a)
ls2=sorted(b)
print(ls1)
print(ls2)
if len(ls1)!=len(ls2):
    print( "NO")
        
for i in range(0,len(ls1)):
    if ls1[i]!=ls2[i]:
        print("NO")
        break
print("YES")
        