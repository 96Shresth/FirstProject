# Please write a program using a generator to print the numbers which can be
# divisible by 5 and 7 between 0 and n in comma separated form while n is
# input by console.

# Example:
# If the following n is given as input to the program:
# 100
# Then, the output of the program should be: 0,35,70
n=int(input('enter the number here: '))
def gen(n):
  
  i=1
  while i<n:
    if (i+1)%7==0 and (i+1)%5==0:
      yield i+1
    i+=1
x=gen(n)
divBy = [i for i in x ]
print(divBy)