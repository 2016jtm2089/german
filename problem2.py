import random
import math

count=0
n=100
for i in range(n):
  (x,y)=(random.random()*2- 1, random.random()*2-1)
 # print x,y
  z=math.sqrt(x*x+y*y)
  if z<1:
    count+=1
   
#print count
p=(count*100)/n  
print p  
  


