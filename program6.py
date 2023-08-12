price=int(input("enter price of cake"))
quantity=int(input("enter number of cakes"))
amount=price*quantity
if (quantity>5):
    discount=amount *10/100
else:
    discount=0
tax=(amount-discount) *5/100
finalamount=tax-discount+tax
print(amount)
print(discount)
print(tax)
print(finalamount)    