import pandas as pd
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Student_data_Project\output\cleaned_data.csv")
print("Module 3: Data Cleaning")
#  Remove Duplicate Records
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
