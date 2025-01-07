# input Data
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

# grade for every deer
for department in department_list:
      for i in range(2):
            scores = students[department][i]["grades"]["scores"] * 3
            participation = students[department][i]["grades"]["participation"] * 5
            social_behavior = students[department][i]["grades"]["social_behavior"] * 2
            grade = (scores + participation + social_behavior) / 10
            students[department][i]["grades"] = grade
print(students)