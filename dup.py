def has_duplicates(lst):
   seen = set()
   for item in lst:
      if item in seen:
         return True
      seen.add(item)
   return False
   
print(has_duplicates(["a","b","d","c"]))