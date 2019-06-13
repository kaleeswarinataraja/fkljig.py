a,b=input().split()
a=int(nu)
b=int(mu)
for i in range(a+1,b):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
        break

    else:
      print(i,end=' ')
  else:
    break
