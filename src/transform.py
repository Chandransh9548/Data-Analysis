import pandas as pd
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Student_data_Project\output\cleaned_data.csv")
print("Module4: Data Transformation ")
#  Create Grade Column
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
print(df.head())
# Save the transformed dataset
df.to_csv("output/cleaned_data.csv", index=False)

print("\nData Transformation Completed Successfully!")
