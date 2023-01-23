def double_stuff(x):
  for b in x:
    b *= 2
    print(b)
  return x

print(double_stuff([6.7, 5,"seven"]))