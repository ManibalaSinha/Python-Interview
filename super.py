class Parent:
   def greet(self):
      print("helooo from Parent")
class Child(Parent):
   def greet(self):
      super().greet()
      print("Hello from child")
c= Child()
c.greet()