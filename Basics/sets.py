skills = {"Python", "Java", "C++"}

skills.add("Machine Learning")

skills.update(["NLP", "Deep Learning"])

skills.discard("Java")

print(skills)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B) #not matched in both sets