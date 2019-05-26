num1=int(input("Enter a first number : "))
num2=int(input("Enter a second number : "))

def divisible (num1 ,num2):
   if num1%num2 == 0 :
      print("Number 1 is completely divisible by Number 2")
   else:
      print("Number 1 is  not completely divisible by Number 2")


divisible(num1,num2)