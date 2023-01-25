#gives function "double_stuff"
def double_stuff(x):
  #doubles whatever is put into the list regardless if its an index or not
  for b in x:
    b *= 2
    print(b)
  return x
#should get 13.4, 10, sevenseven
print(double_stuff([6.7, 5,"seven"]))
#should get 2, 14, 44
print(double_stuff([1, 7, 22]))
#should get 2.2, 686.8, and 6
print(double_stuff([1.1, 343.4, 3]))