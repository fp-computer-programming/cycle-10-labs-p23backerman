


#gives base values for the functions ans statements
total = 0
ele = 0
list = [0, 0]  
A1 = 0
#if A1 is still A1, the loops will continue until the break
while A1 == A1:
  #asks the user for a number and that number will be added to the end of the list 
  print("give a number")
  A = input()
  A1 = int(A) 
  list.append(A1)
  #once the used puts in -1, the loop ends and it will be printed
  if A1 == -1:
    break
print(list)
#while the list length is still greater than the number being added, the loop continues until all of the numbers have been added together
while(ele < len(list)):
    total = total + list[ele]
    ele += 1
#adds an extra one to get rid of the -1 input
Sum = total + 1
print(Sum)

