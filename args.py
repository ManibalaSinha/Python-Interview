def my_function(*args):
   for arg in args:
      print(arg)
my_function(10,20,25)
def my_func(**kwargs):
   for key, value in kwargs.items():
      print(f"{key}={value}")
my_func(name = "Alice", age=30, city="Vaughan")