name = "Tommy Yick"
age = 25
gpa = 3.20
is_student = False
is_coder= True

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I have a GPA of {gpa}")
print(f"Am I a student? {is_student}")

print(name[0:3])
print(name.upper())
print(len(name))

print(f"Age in months: {age * 12}")
print(f"Age in days: {age * 365}")
print(f"Age in 10 years from now: {age + 10}")

print(f"Am I a student and a coder? {is_student and is_coder}")
print(f"Am I a student or a coder? {is_student or is_coder}")
print(f"It is false that I am a student {not is_student}")
