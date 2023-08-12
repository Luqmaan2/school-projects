#DECLARE M: ARRAY[1:10] OF INTEGER
M = [0 for Count in range(10)]
for Index in range(10):
 M[Index] = int(input("Enter number: "))
#ENDFOR
for Index in range(9,-1,-1):
 print(M[Index])