import pandas as pd

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Student_data_Project\output\cleaned_data.csv")

print("Module 5: Data Filtering")

# Top-performing students (Marks >= 90)
toppers = df[df["Marks"] >= 90]

# Failed students
failed_students = df[df["Result"] == "Fail"]

# Students with attendance below 75%
low_attendance = df[df["Attendance"] < 75]

# Students studying more than 8 hours
high_study = df[df["StudyHours"] > 8]

# Save only the required files
toppers.to_csv("output/toppers.csv", index=False)
failed_students.to_csv("output/failed_students.csv", index=False)

# Display results
print("\n===== Top Performing Students =====")
print(toppers)

print("\n===== Failed Students =====")
print(failed_students)

print("\n===== Students with Attendance Below 75% =====")
print(low_attendance)

print("\n===== Students Studying More Than 8 Hours =====")
print(high_study)

print("\nFiltering completed successfully.")
