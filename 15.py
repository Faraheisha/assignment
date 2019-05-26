amt=int(input("Enter amount :"))
interest=float(input("Enter rate of interest :"))
year=int(input("Enter a  number of years:"))
future_value=amt * ((1+(0.01*interest))) ** year
print("The future value will be :",round(future_value,2))