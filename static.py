class Book:
   default_genre = "Fiction"
   def __init__(self, title, genre=None):
      self.title=title
      self.genre = genre or Book.default_genre
   @classmethod
   def change_default_genre(cls, genre):
      cls.default_genre= genre
Book.change_default_genre("Sci-Fi")
b= Book("Dune")
print(b.genre)

class MathUtils:
   @staticmethod
   def add(a,b):
      return a+b
print(MathUtils.add(3,7))
