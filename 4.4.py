a=input().split()
m=a.count(a[0])
k=a[1]
for i in range(len(a)):
  if a.count(a[i])>m:
      k=a[i]
print(k)

