#Program to Find the Roots of a Quadratic Equa
a = int(input("Enter a  : "))
b = int(input("Enter b : "))
c = int(input("Enter c :  ")) # x = [-b ± sqrt(b**2 - 4ac)] / (2a)
ans = (b*b) - (4*a*c)
ans = ans**0.5
root1 = (-b + ans)/(2*a)
root2 = (-b - ans/ (2*a))
print("Root1 :  ", root1)
print("Root2 ", root2)

 