print("Input your height in feets: ")
h_ft = int(input("Feet: "))
h_inchs=h_ft*12
h_yards=h_ft/3.0
h_miles=h_ft/5280.0
print("The height in inches is :%i inches" %h_inchs)
print("The height in yards is : %.3f yards " %h_yards)
print("The height in miles is :%.3f miles" %h_miles)
