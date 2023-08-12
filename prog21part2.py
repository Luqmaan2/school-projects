Temp = [0 for Count in range (2)]
for Index in range (2):
 Temp[Index] = float(input("Enter temperature: "))
for Index in range (2):
 Fahrenheit = Temp[Index] * 1.8 + 32
print(Temp[Index],"°C=",Fahrenheit,"°F")