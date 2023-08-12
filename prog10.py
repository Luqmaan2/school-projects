#tute 17
Lowest = 999
H = -999
m=0
while m <= 3:
 Temp= int(input("Enter temperature "))
 if Temp > H:
     H = Temp
#ENDIF
 if Temp < Lowest:
     Lowest = Temp
#endif
 m = m + 1  
#ENDWHILE
print("Highest temp = ",H)
print("Lowest temp = ",Lowest)