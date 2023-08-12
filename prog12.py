#tute 19
Total = 0
Quantity = 0
while Quantity != -1:
 Quantity = int(input("Enter qty: "))
 if Quantity!= -1:
  Price = int(input("Enter price: "))
  Amount = Quantity*Price
  print("Amount = ",Amount)
  Total = Total + Amount
#ENDWHILE
print("Total = ",Total)