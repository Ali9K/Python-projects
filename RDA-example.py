# Input Data
department_list = ["Computer Engineering", "Electrical Engineering", "Mechanical Engineering"]

students = {
    'Computer Engineering': [
        {"name": "Ali", "grades": {"scores": 85, "participation": 90, "social_behavior": 80}},
        {"name": "Sara", "grades": {"scores": 78, "participation": 88, "social_behavior": 85}},
    ],
    'Electrical Engineering': [
        {"name": "Noura", "grades": {"scores": 90, "participation": 85, "social_behavior": 87}},
        {"name": "Sina", "grades": {"scores": 84, "participation": 89, "social_behavior": 78}},
    ],
    'Mechanical Engineering': [
        {"name": "Alireza", "grades": {"scores": 92, "participation": 88, "social_behavior": 85}},
        {"name": "Shirin", "grades": {"scores": 80, "participation": 82, "social_behavior": 89}},
    ],
}

# Initialization of the Population
for department in department_list:
    for student in students[department]:
        scores = student["grades"]["scores"] * 3
        participation = student["grades"]["participation"] * 5
        social_behavior = student["grades"]["social_behavior"] * 2
        grade = (scores + participation + social_behavior) / 10
        student["fitness"] = grade

# Dominant Male Selection (Top student per department)
selected_students = {}
for department in department_list:
    selected_students[department] = max(students[department], key = lambda x: x["fitness"])

# Group Combination (Mating)
generation = 1
max_generations = 3  # Number of iterations to improve
while generation <= max_generations:
    combined = []
    for student in selected_students.values():
        combined.append(student)

    # Simulate a basic crossover between "dominant" students
    next_generation = []
    for i in range(len(combined)):
        for j in range(i + 1, len(combined)):
            parent1, parent2 = combined[i], combined[j]
            offspring_fitness = (parent1["fitness"] + parent2["fitness"]) / 2
            offspring_name = "Offspring of %s and %s" %(parent1['name'], parent2['name'])
            next_generation.append({"name": offspring_name, "fitness": offspring_fitness})

    # Combine new generation with original dominant students
    combined.extend(next_generation)

    # Select the best student from the new generation
    best_student = max(combined, key=lambda x: x["fitness"])

    print(f"Generation {generation}: Best student is {best_student['name']} with fitness {best_student['fitness']}")

    generation += 1

# Final Selection
print("The representative is:", best_student["name"])
