#calculation of body mass index
# tThe formula of BMI is wight/height^2
height = float(input("Input your height in meters: "))
weight = float(input("Input your weight in kilogram: "))
BMI=weight / (height * height)
print("Your body mass index is: ", round(BMI, 2))