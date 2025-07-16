s1="hello"
s2="world"
combine= s1+s2
print(combine)
substring = combine[1:4]
print(substring.upper()) #ell
print(substring.lower())
print(substring.capitalize())
print(substring.title())
print(s1.swapcase())
print(combine.find("world"))
name = "Alice"
age=30
formatted = f"Name: {name}, Age: {age}"
print(formatted)