import math
n = 10
isPrime = [True]*(n+1)
l = int(math.sqrt(n))
for i in range(2, l):
      if isPrime[i]==False:
         pass
      else:
         for j in range(3, n+1):
            if j%i==0:
               isPrime[j]=False
isPrime[0] = False
isPrime[1] = False

print(isPrime)