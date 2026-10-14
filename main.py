import pandas as pd
import numpy as np
from functions import get_grade
data = pd.read_csv("students.csv")
subjects = ["Python", "Mathematics", "AI", "Data Analysis", "English"]
marks = data[subjects].to_numpy()
data["Total"] = np.sum(marks, axis=1)
data["Average"] = np.round(np.mean(marks, axis=1), 2)
grades = []
results = []
for i in range(len(data)):
    grades.append(get_grade(data.loc[i, "Average"]))
    if np.min(marks[i]) >= 40 and data["Attendance"].iloc[i] >= 75:
        results.append("Pass")
    else:
        results.append("Fail")
        
data["Grade"] = grades
data["Result"] = results
print("\nSTUDENT RESULT")
print(data[["Name", "Total", "Average", "Grade", "Attendance", "Result"]].to_string(index=False))

print("\nHIGHEST MARKS")
max_marks = data["Total"].max()
topper = data[data["Total"] == max_marks]
print(topper[["Name", "Total"]].to_string(index=False))

print("\nLOWEST MARKS")
min_marks = data["Total"].min()
lowest = data[data["Total"] == min_marks]
print(lowest[["Name", "Total"]].to_string(index=False))

print("\nTOP 3 STUDENTS")
top_students = data.sort_values("Total", ascending=False).head(3)
print(top_students[["Name", "Total", "Average", "Grade"]].to_string(index=False))

print("\nCLASS SUMMARY")
print("Total student:", len(data))
print("Pass student:", results.count("Pass"))
print("Fail student:", results.count("Fail"))
print("\nSUBJECT AVERAGE")
for subject in subjects:
    print(subject, ":", round(np.mean(data[subject]), 2))
data.to_csv("result.csv", index=False)
print("\nResults saved in result.csv")
