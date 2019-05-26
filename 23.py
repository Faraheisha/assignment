temp=input("Enter your temperatutre in celcius and fahrenheit: ")
s=temp.split(",")
temp_cel=int(s[0])
temp_feh=int(s[1])
temp_fah=(temp_cel*9/5)+32
temp_cel=(temp_feh-32)*5/9
print("The temperature in celcius is :" ,round(temp_cel,2))
print("The temperature in fahrenheit is :" ,round(temp_fah,2))

