def count_up_to(n):
   count =1
   while count<=n:
      yield count
      count +=1
gen = count_up_to(3)
for num in gen:
   print(num) 

squares =(x*x for x in range(5))
print(next(squares))
print(next(squares))
print(next(squares))