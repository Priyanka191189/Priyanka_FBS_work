# Convert distant given in feet and inches into meter and centimeter.
feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))
# 1 foot = 12 inch
# 1 inch = 0.0254 meter
# 1 foot = 12*0.0254 = 0.3048 meter
feet_meter = feet*0.3048
# 1 inch = 0.0254 meter
# 1 inch = 0.0254*100= 2.54 cm
inch_centimeter = inches*2.54
print("Feet_Meter:  ", feet_meter)
print("Inches to Centimeter: ", inch_centimeter)
