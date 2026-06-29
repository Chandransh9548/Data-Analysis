import pandas as pd
print("Module 7:Sorting")
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Student_data_Project\output\cleaned_data.csv")

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

