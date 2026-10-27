"""Reusable functions for the Student Performance Analytics System."""
import numpy as np
import pandas as pd

SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "Computer_Science"]
PASS_MARK = 35          # minimum marks needed in EVERY subject to pass
MIN_ATTENDANCE = 75     # attendance % below this is flagged as shortage


def load_data(path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(path)


def calculate_total_and_average(df):
    """Add Total and Average columns using NumPy on the subject marks."""
    marks = df[SUBJECTS].to_numpy()                 # DataFrame -> NumPy array
    df["Total"] = np.sum(marks, axis=1)             # row-wise sum
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def assign_grade(average):
    """Grading rule: map an average mark to a letter grade."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B+"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    return "F"


def add_grades(df):
    """Loop over every student's average and store the grade."""
    grades = []
    for avg in df["Average"]:
        grades.append(assign_grade(avg))
    df["Grade"] = grades
    return df


def add_result_status(df):
    """Pass only if the student scored >= PASS_MARK in every subject."""
    results = []
    for _, row in df.iterrows():
        subject_marks = row[SUBJECTS].to_numpy(dtype=float)
        if np.all(subject_marks >= PASS_MARK):
            results.append("Pass")
        else:
            results.append("Fail")
    df["Result"] = results
    df["Attendance_Status"] = np.where(
        df["Attendance"] >= MIN_ATTENDANCE, "OK", "Shortage"
    )
    return df


def subject_analysis(df):
    """Average, highest, lowest and pass count for each subject."""
    rows = []
    for subject in SUBJECTS:
        marks = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Average": round(float(np.mean(marks)), 2),
            "Highest": int(np.max(marks)),
            "Lowest": int(np.min(marks)),
            "Passed": int(np.sum(marks >= PASS_MARK)),
        })
    return pd.DataFrame(rows)


def department_analysis(df):
    """Average marks and pass count per department."""
    return (df.groupby("Department").agg(Students=("Student_ID", "count"),
                   Avg_Marks=("Average", "mean"),
                   Passed=("Result", lambda r: (r == "Pass").sum())).round(2).reset_index())


def top_performers(df, n=3):
    """Return the top-n students by average marks."""
    return df.nlargest(n, "Average")[["Student_ID", "Name", "Department", "Average", "Grade"]]


def class_summary(df):
    """Overall class statistics as a dictionary."""
    avg = df["Average"].to_numpy()
    return {
        "Total students": len(df),
        "Passed": int((df["Result"] == "Pass").sum()),
        "Failed": int((df["Result"] == "Fail").sum()),
        "Pass percentage": round(float((df["Result"] == "Pass").mean() * 100), 2),
        "Class average": round(float(np.mean(avg)), 2),
        "Highest average": float(np.max(avg)),
        "Lowest average": float(np.min(avg)),
        "Attendance shortage": int((df["Attendance_Status"] == "Shortage").sum()),
    }
