# You are required to write a program to sort the (name, age, height) tuples by
# ascending order where name is string, age and height are numbers. The
# tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
lst = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
list2=[]
# iterating till the range
for i in range(0, n):
  for j in range(2):
    if j==0:
      name=str(input('enter name: ' ))
      list2.append(name)
    if j==1:
      age=int(input('enter age: '))
      list2.append(age)
    else:
      score=int(input('enter score: '))
      list2.append(score)
  tp=tuple(list2)
  list2=[]
  lst.append(tp)
  

  
    
sorted_list = sorted(
lst,
key=lambda t: (t[0],t[1], t[2]))


print(sorted_list) 
print(lst)