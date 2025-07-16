def add(x,y):
   return x+y
print(add(2,3))
add = lambda x,y: x+y
print(add(4, 5))
nums =[1,2,3,4]
squared= list(map(lambda x:x**2, nums))
print(squared)