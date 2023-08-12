total=0
count=0
while True:
    temp=int(input("enter the tempurature"))
    if temp>=0:
        total=total+temp
        count=count+1
    if temp <0 :break    
avg=total/count
print(avg)    