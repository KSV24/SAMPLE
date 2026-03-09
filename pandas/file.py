#import numpy as np
import pandas as pd

#def generate_school_data(students=10, seed=42):
    #np.random.seed(seed)
    #math = np.random.randint(35, 100, students)
    #science = np.random.randint(35, 100, students)
   # english = np.random.randint(35, 100, students)
   # attendance = np.random.randint(60, 100, students)
   # study_hours = np.random.randint(1, 20, students)
   # df = pd.DataFrame({
    #    "Math": math,
     #   "Science": science,
     #   "English": english,
    #    "Attendance": attendance,
   #     "Study_Hours": study_hours
  #  })
 #   return df
#school_df = generate_school_data()
#print(school_df)

#print(school_df.head())
#print(school_df.info())
#print(school_df.describe())
#print(school_df.shape)

dataset = pd.read_csv(r"C:\Users\Vishal KS\OneDrive\Desktop\New folder\pandas\data.csv")
#print(dataset)

#print(dataset.head())
#print(dataset.tail())
#print(dataset.info())
#print(dataset.describe())

print(dataset['gender'])