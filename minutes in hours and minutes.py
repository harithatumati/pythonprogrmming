n=int(input())
p=n%60
q=n/60
c=[]
c.append(q)
c.append(p)
d=" ".join(map(str,c))
print(d)
