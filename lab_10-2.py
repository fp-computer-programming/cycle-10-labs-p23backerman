#gives base values for the functions ans statements
total = 0
ele = 0
list = []  
A1 = 0
#if A1 is still A1, the loops will continue until the break
while A1 != -1:
  #asks the user for a number and that number will be added to the end of the list if it is divisible by 3 
  print("give a number")
  A = input()
  A1 = int(A) 
  if A1 % 3 == 0:
    list.append(A1)
  #once the used puts in -1, the loop ends and it will be printed
  if A1 != -1:
    continue
print(list)


