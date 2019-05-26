def triangle(b,h):
    area=(1/2)*(b*h)
    return area
b=int(input("Enter a base  :"))
h=float(input("Enter a height  :"))
area=triangle(b,h)
print("The computed area of triangle is : ",area)
