# Tien Phan
# list practice with Python

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 87, 85, 88]
subjects.append("computer science")
grades.append(100)

gradebook = list(zip(subjects, grades))

gradebook.append(("visual arts", 93))

full_gradebook = gradebook + last_semester_gradebook
print(list(gradebook))
print("\n")
print(list(full_gradebook))
