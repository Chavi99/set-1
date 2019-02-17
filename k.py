ls=[]
x=list(map(int,input().split(" ")))
n=x[0]
k=x[1]
ls=list(map(int,input().split(" ")))
c=0
sum=0
for i in ls:
    sum+=i
    c+=1
    if c==k:
        break
print(sum)
