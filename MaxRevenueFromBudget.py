T = int(input())
mylist=[]
for i in range(T):
    mylist.append(int(input()))
mylist.sort()
resultlist=[]
for i in range(0,T):
    resultlist.append(mylist[i]*(T-i))
print(max(resultlist))
    
