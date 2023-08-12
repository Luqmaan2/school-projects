#tute 41
M = [0 for Index in range(10)]
#DECLARE Odd : ARRAY[0:9] OF INTEGER
Odd = [0 for Index in range(10)]
for Index in range(10):
 M[Index] = int(input("Enter mark "))
#ENDFOR
E = 0
for Index in range(10):
 if M[Index] % 2 == 1:
  Odd[E] = M[Index]
 E = E + 1
 #ENDIF
#ENDFOR
for Index in range(E):
 print(Odd[Index])