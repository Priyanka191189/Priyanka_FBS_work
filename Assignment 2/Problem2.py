#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)
celsius = float(input("Enter Temp in Celcius:  "))  
#celsius = ((F-32)*5)/9
F = celsius * 9/5 +32
print("Temp in Fahrenheit:  ", F)