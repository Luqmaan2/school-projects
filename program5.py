hourlyrate=int(input("enter hourly rate"))
hours=int(input("enter number of hours "))
wage=hourlyrate*hours
if wage>2000:
    tax=wage *5/100
else:
    tax=0
netwage=wage-tax
print(wage)
print(tax) 
print(netwage)       