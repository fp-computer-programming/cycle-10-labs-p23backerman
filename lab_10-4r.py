#the values that will be put in the function
b = ["John", "Jane", "Bob"]
#sets b2 to equal nothing so things can be added
b2 = []
#gives the function indexed_names where it will identify the index and the value to enumerate each value in a list to have their index, a colon, and the og value
def indexed_names(x):
  for i, v in enumerate(x):
    a = "{0}: {1}".format(i, v)
    b2.append(a)
  return b2


#tests hows its supposed to work
print(indexed_names(b))
#tests to make sure it adds to the previous list
print(indexed_names(["john"]))