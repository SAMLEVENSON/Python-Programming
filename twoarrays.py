a=int(input())
c=int(input())
b=[]
d=[]
for a in range(a):
    b.append(int(input()))
for c in range(c):
    d.append(int(input()))
for e in d:
    if e in b:
        print("YES")
    else:
        print("NO")
