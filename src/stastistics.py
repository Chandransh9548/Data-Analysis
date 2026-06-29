import pandas as pd
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Student_data_Project\output\cleaned_data.csv")
print("Module 9:Statistical Analysis")


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

