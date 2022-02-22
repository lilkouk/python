import time
def fibo(n):
   a=0
   b=1
   cpt=0
   while cpt< n:
       a,b= b,a+b
       cpt=cpt+1
   return b

for i in range (20000):
    print("fibonacci de ", i , "  est ==>", fibo(i))
print (time.process_time())