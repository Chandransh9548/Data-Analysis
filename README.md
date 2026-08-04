# Student Marks Prediction Based on Study Hours and Attendance

## Project Overview

The Student Data Project is a Python-based data analysis project developed using the Pandas library. It demonstrates the complete data analysis workflow, including data loading, inspection, cleaning, transformation, filtering, analysis, sorting, grouping, statistical analysis, and report generation.

---

## Objectives

* Load and inspect student data.
* Clean and validate the dataset.
* Transform data by creating new columns.
* Filter students based on different conditions.
* Perform statistical and descriptive analysis.
* Sort and group student records.
* Generate a final project report.

---

## Technologies Used

* Python 3
* Pandas

---

## Project Folder Structure

```text
Student_Data_Project/
│
├── data/
│   └── student_dataset_v2.csv
│
├── output/
│   ├── cleaned_data.csv
│   ├── toppers.csv
│   ├── failed_students.csv
│   └── report.csv
│
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── transform.py
│   ├── filter_data.py
│   ├── analyze.py
│   ├── sorting.py
│   ├── grouping.py
│   ├── statistics.py
│   └── report.py
│
├── main.py
│
└── README.md
```

---

## Modules

### Module 1: Data Loading

* Load the student dataset.
* Display first and last records.
* Display dataset shape, columns, and data types.

### Module 2: Data Inspection

* Check missing values.
* Check duplicate records.
* Display descriptive statistics.
* Display memory usage.
* Display dataset summary.

### Module 3: Data Cleaning

* Remove duplicate records.
* Handle missing values.
* Validate marks, attendance, and study hours.
* Save the cleaned dataset.

### Module 4: Data Transformation

* Create Grade column.
* Create Result column.
* Create Performance Score column.

### Module 5: Data Filtering

* Top-performing students.
* Failed students.
* Students with attendance below 75%.
* Students studying more than 8 hours.

### Module 6: Data Analysis

* Average marks.
* Highest marks.
* Lowest marks.
* Average attendance.
* Average study hours.
* Pass percentage.
* Fail percentage.
* Grade distribution.

### Module 7: Sorting

* Sort students by marks.
* Sort students by attendance.
* Sort students by study hours.

### Module 8: Grouping

* Average marks by grade.
* Number of students in each grade.
* Average attendance by grade.

### Module 9: Statistical Analysis

* Mean
* Median
* Mode
* Standard Deviation
* Variance
* Correlation Matrix

### Module 10: Report Generation

Generate a final report containing:

* Total Students
* Passed Students
* Failed Students
* Highest Marks
* Lowest Marks
* Average Marks
* Average Attendance
* Grade-wise Distribution

---

## Output Files

The project generates the following output files:

* cleaned_data.csv
* toppers.csv
* failed_students.csv
* report.csv

---

## How to Run the Project

1. Install Python 3.
2. Install Pandas using:

```bash
pip install pandas
```

3. Place `student_dataset_v2.csv` inside the `data` folder.
4. Run `main.py`.

---

## Author

**Name:** Chandransh

**Project:** Student Marks Prediction Based on Study Hours and Attendance

**Language:** Python

**Library:** Pandas
