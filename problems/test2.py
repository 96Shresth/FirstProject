# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
def gen(n):
  i=1
  while i<n:
    if (i+1)%7==0:
      yield i+1
    i+=1
x=gen(55)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
