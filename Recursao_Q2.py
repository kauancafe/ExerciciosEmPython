def elev(x, n):
     if n == 0: 
         return 1
     else: 
         return x * elev(x, n - 1)

print(elev(0, 1))