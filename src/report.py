import pandas as pd
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Student_data_Project\output\cleaned_data.csv")
print("Module 10: Report Generarion")
df = pd.read_csv("output/cleaned_data.csv")
# Total Students
total_students = len(df)

# Number of Passed Students
passed_students = (df["Result"] == "Pass").sum()

# Number of Failed Students
failed_students = (df["Result"] == "Fail").sum()

# Highest Marks
highest_marks = df["Marks"].max()

# Lowest Marks
lowest_marks = df["Marks"].min()

# Average Marks
average_marks = df["Marks"].mean()

# Average Attendance
average_attendance = df["Attendance"].mean()

# Grade-wise Distribution
grade_distribution = df["Grade"].value_counts()

# Create Report DataFrame
report = pd.DataFrame({
    "Total Students": [total_students],
    "Passed Students": [passed_students],
    "Failed Students": [failed_students],
    "Highest Marks": [highest_marks],
    "Lowest Marks": [lowest_marks],
    "Average Marks": [round(average_marks, 2)],
    "Average Attendance": [round(average_attendance, 2)]
})

# Save report
report.to_csv("output/report.csv", index=False)

# Save Grade Distribution
grade_distribution.to_csv("output/grade_distribution.csv", header=["Student Count"])

# Display Report
print("\n========== FINAL REPORT ==========\n")
print(report)

print("\n========== GRADE-WISE DISTRIBUTION ==========\n")
print(grade_distribution)

print("\nReport saved successfully.")
print("Files created:")
print("1. output/report.csv")
print("2. output/grade_distribution.csv")