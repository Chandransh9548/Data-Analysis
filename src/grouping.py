import pandas as pd
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Student_data_Project\output\cleaned_data.csv")
print("Module 8: Grouping")
# 1. Average Marks by Grade
average_marks = df.groupby("Grade")["Marks"].mean()

# 2. Number of Students in Each Grade
student_count = df.groupby("Grade").size()

# 3. Average Attendance by Grade
average_attendance = df.groupby("Grade")["Attendance"].mean()

# Display Results
print("========== GROUPING REPORT ==========\n")

print("Average Marks by Grade")
print(average_marks)

print("\nNumber of Students in Each Grade")
print(student_count)

print("\nAverage Attendance by Grade")
print(average_attendance)

# Save report into CSV
group_report = pd.DataFrame({
    "Average Marks": average_marks,
    "Student Count": student_count,
    "Average Attendance": average_attendance
})

group_report.to_csv("output/group_report.csv")

print("\nGrouping report saved successfully.")

