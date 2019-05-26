def compare(num1,num2):
    if num1==num2 or (num1+num2)==5 or (num1-num2)==5:
       return True
    return False
          

num1=int(input("Enter a number1 :"))
num2=int(input("Enter a number2 :"))
s=compare(num1,num2)
print(s)