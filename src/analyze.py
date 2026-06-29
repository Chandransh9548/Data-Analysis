import pandas as pd
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Student_data_Project\output\cleaned_data.csv")
#  Average Marks
average_marks = df["Marks"].mean()

#  Highest Marks
highest_marks = df["Marks"].max()

#  Lowest Marks
lowest_marks = df["Marks"].min()

#  Average Attendance
average_attendance = df["Attendance"].mean()

#  Average Study Hours
average_study_hours = df["StudyHours"].mean()

#  Pass Percentage
pass_percentage = (df["Result"] == "Pass").mean() * 100

#  Fail Percentage
fail_percentage = (df["Result"] == "Fail").mean() * 100

#  Grade Distribution
grade_distribution = df["Grade"].value_counts()

print("Display Result")
print("========== Data Analysis ==========")

print("Average Marks:", round(average_marks, 2))

print("Highest Marks:", highest_marks)

print("Lowest Marks:", lowest_marks)

print("Average Attendance:", round(average_attendance, 2))

print("Average Study Hours:", round(average_study_hours, 2))

print("Pass Percentage:", round(pass_percentage, 2), "%")

print("Fail Percentage:", round(fail_percentage, 2), "%")

print("\nGrade Distribution:")
print(grade_distribution)

