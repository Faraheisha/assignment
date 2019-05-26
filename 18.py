import math
def hypoteneus(a,b):
   x=math.pow(a,2)
   y=math.pow(b,2)
   result=math.sqrt(x+y)
   return result
a= int(input("input base: "))
b= int(input("input height: "))
result=hypoteneus(a,b)
print("The calculated hytoteneus of right angled triangle is : ",round(result,3))