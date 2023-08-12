def Grade(m):
 if m >=80:
    print("A")
 elif m>=60 and m<=79:
   print("B")
 elif m>=50 and m<=59:
   print("c")
 else:
   print("X")  


mark=int(input("enter your grade "))
Grade(mark)