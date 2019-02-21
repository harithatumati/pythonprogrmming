n=int(input())
b=1
c=[]
c.append(b)
for x in range(0,n-1):
    a=1
    a=a+x
    c.append(a)
h=' '.join(map(str,c))
print(h)
