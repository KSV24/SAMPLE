import numpy as np

def generate_school_data(students=100, seed=42):
    np.random.seed(seed)
    math = np.random.randint(35, 100, students)
    science = np.random.randint(35, 100, students)
    english = np.random.randint(35, 100, students)
    attendance = np.random.randint(60, 100, students)
    study_hours = np.random.randint(1, 20, students)
    data = np.column_stack((math, science, english, attendance, study_hours))
    return data
school_data = generate_school_data(10)
print("School Dataset:\n", school_data)
print("Shape:", school_data.shape)