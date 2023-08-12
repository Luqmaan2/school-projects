#tute 39
M = [0 for Index in range(15)]
for Index in range(15):
 M[Index] = int(input("Enter a mark "))
#ENDFOR
for Index in range(15):
 Per = M[Index] / 75 * 100
 print(Per)