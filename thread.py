from threading import *
import time
def fibo(n):
   a=0
   b=1
   cpt=0
   while cpt< n:
       a,b= b,a+b
       cpt=cpt+1
   return b



class Hello (Thread):
    def run(self) -> None:
        for i in range (10000):
          print("fibonacci de== ", i , "  est ==>", fibo(i))
        print (time.process_time())
            
class Bonjour (Thread):
    def run(self) -> None:
        
        for i in range (3000):
            print("fibonacci de ", i , "  est ==>", fibo(i))
        print (time.process_time()/60)
t1=Hello()
t2=Bonjour()
t3=Hello()
t4=Bonjour()
t5=Hello()
t6=Bonjour()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()


