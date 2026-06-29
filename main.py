
import pandas as pd
print("  Module1: Data Loading")
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Student_data_Project\data\student_dataset_v2.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)


print("Module 2:  Data Inspection")
print("Missing Values")
print(df.isnull().sum())
print("\n----- Duplicate Records -----")
print("Number of Duplicate Rows:", df.duplicated().sum())
print("\n----- Descriptive Statistics -----")
print(df.describe())
print("\n----- Memory Usage -----")
print(df.memory_usage())
print("\n----- Summary Information -----")
df.info()

print("Module 3: Data Cleaning")
# Remove Duplicate Records
df.drop_duplicates(inplace=True)
# Fill missing numeric values with the column average
df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
# Remove rows where StudyHours, Attendance, or Marks are negative
df = df[(df["StudyHours"] >= 0) &
        (df["Attendance"] >= 0) &
        (df["Marks"] >= 0)]

#  Validate Attendance Values (0 to 100)
df = df[df["Attendance"] <= 100]

#  Validate Study Hours (0 to 24)
df = df[df["StudyHours"] <= 24]

#  Validate Marks (0 to 100)
df = df[df["Marks"] <= 100]

# Display Cleaned Data
print("Cleaned Dataset")
print(df.head())

# Save Cleaned Dataset
df.to_csv("output/cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully as output/cleaned_data.csv")


# Load the cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")

# ==========================
# Module 4 : Data Transformation
# ==========================

# 1. Create Grade Column
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(grade)

# 2. Create Result Column
def result(mark):
    if mark >= 40:
        return "Pass"
    else:
        return "Fail"

df["Result"] = df["Marks"].apply(result)

# 3. Create Performance Score Column
df["PerformanceScore"] = (
    (df["Marks"] * 0.6) +
    (df["Attendance"] * 0.3) +
    (df["StudyHours"] * 2)
)

# Display the updated dataset
print(df.head())

# Save the transformed dataset
df.to_csv("output/cleaned_data.csv", index=False)

print("\nData Transformation Completed Successfully!")

# Module 5 : Data Filtering

#  Top-performing students (Marks >= 90)
toppers = df[df["Marks"] >= 90]

#  Failed students
failed_students = df[df["Result"] == "Fail"]

#  Students with attendance below 75%
low_attendance = df[df["Attendance"] < 75]

#  Students studying more than 8 hours
high_study = df[df["StudyHours"] > 8]

# Save all filtered datasets

toppers.to_csv("output/toppers.csv", index=False)

failed_students.to_csv("output/failed_students.csv", index=False)

low_attendance.to_csv("output/low_attendance.csv", index=False)

high_study.to_csv("output/high_study_hours.csv", index=False)

# Display the datasets

print("\n===== Top Performing Students =====")
print(toppers)

print("\n===== Failed Students =====")
print(failed_students)

print("\n===== Students with Attendance Below 75% =====")
print(low_attendance)

print("\n===== Students Studying More Than 8 Hours =====")
print(high_study)

print("\nAll filtered datasets have been saved successfully.")

print("Module 6: Data Analysis")

# Load the cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")

# Load the cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")


# Module 6 : Data Analysis
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


print("Module 7:Sorting")
df = pd.read_csv("output/cleaned_data.csv")
# Load cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")

print("========== Students Sorted by Marks ==========")
marks_sorted = df.sort_values(by="Marks", ascending=False)
print(marks_sorted)

print("\n========== Students Sorted by Attendance ==========")
attendance_sorted = df.sort_values(by="Attendance", ascending=False)
print(attendance_sorted)

print("\n========== Students Sorted by Study Hours ==========")
studyhours_sorted = df.sort_values(by="StudyHours", ascending=False)
print(studyhours_sorted)

# Save sorted datasets
marks_sorted.to_csv("output/sorted_by_marks.csv", index=False)
attendance_sorted.to_csv("output/sorted_by_attendance.csv", index=False)
studyhours_sorted.to_csv("output/sorted_by_studyhours.csv", index=False)

print("\nSorting completed successfully.")


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


print("Module 9:Statistical Analysis")

# Load the cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")

print("========== STATISTICAL ANALYSIS ==========\n")

# Mean
print("Mean")
print(df[["StudyHours", "Attendance", "Marks"]].mean())

# Median
print("\nMedian")
print(df[["StudyHours", "Attendance", "Marks"]].median())

# Mode
print("\nMode")
print(df[["StudyHours", "Attendance", "Marks"]].mode())

# Standard Deviation
print("\nStandard Deviation")
print(df[["StudyHours", "Attendance", "Marks"]].std())

# Variance
print("\nVariance")
print(df[["StudyHours", "Attendance", "Marks"]].var())

# Correlation Matrix
print("\nCorrelation Matrix")
print(df[["StudyHours", "Attendance", "Marks"]].corr())

print("\nStatistical Analysis Completed Successfully.")

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






