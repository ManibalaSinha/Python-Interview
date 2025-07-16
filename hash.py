student_grades={ "Alice":95, "Bob":88, "Charlie":92}
student_grades["David"]=78
bob_grade= student_grades["Bob"]
print(f"Bob's grade:{bob_grade}")
student_grades["Alice"]=98
if "Charlie" in student_grades:
   print("Charlie is in Dictionary")
del student_grades["David"]
print(student_grades)
