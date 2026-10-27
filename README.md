# Student Performance Analytics System

## 1. Project Title
**Student Performance Analytics System**
Student: Himanshu Verma | Course: Python with AI, EWB Courses | GitHub: Himmu725

## 2. Objective
Teachers handling many students need quick answers: who is topping, who failed, which subject is weak, and who has low attendance. Doing this by hand in Excel is slow and error-prone. This project automates that analysis with Python, NumPy and Pandas and prints a clear, readable report.

## 3. Technologies Used
- Python 3
- NumPy (numerical calculations)
- Pandas (DataFrame loading, grouping, analysis)

## 4. Dataset Description
`students.csv` has **20 student records** and **9 columns**:
`Student_ID, Name, Department, Maths, Physics, Chemistry, English, Computer_Science, Attendance`
Departments: CSE, ECE, IT, ME. Marks are out of 100; attendance is a percentage. The data is sample data created for this project.

## 5. Implementation
1. **Load data**: `load_data()` reads the CSV into a DataFrame; shape, columns and missing values are checked.
2. **Totals and averages**: subject marks are converted to a NumPy array and `np.sum` / `np.mean` are applied row-wise.
3. **Grading rule** (`assign_grade`, applied in a loop over averages): A+ ≥ 90, A ≥ 80, B+ ≥ 70, B ≥ 60, C ≥ 50, D ≥ 40, else F.
4. **Pass/Fail rule** (`add_result_status`): a student passes only if marks are ≥ 35 in **every** subject (checked with `np.all`). Attendance below 75% is flagged as "Shortage".
5. **Analysis**: subject-wise stats (loop + NumPy), department-wise stats (Pandas `groupby`), top performers (`nlargest`), class summary and grade distribution.
6. **Output**: results are printed section by section and saved to `results.csv`.

## 6. Key Features
| Function | Purpose |
|---|---|
| `load_data` | Read CSV into DataFrame |
| `calculate_total_and_average` | Total and average per student (NumPy) |
| `assign_grade` / `add_grades` | Letter grade from average |
| `add_result_status` | Pass/Fail and attendance status |
| `subject_analysis` | Average, highest, lowest, pass count per subject |
| `department_analysis` | Department-wise comparison |
| `top_performers` | Top-N students by average |
| `class_summary` | Overall class statistics |

## 7. Output
Run `python main.py`. Full sample output is in [`output.txt`](output.txt). Key results:

- Class average: **70.15** | Passed: **19/20 (95%)**
- Top performer: **Sneha Tiwari (93.0, A+)**, followed by Divya Mehta and Priya Singh
- Best subject: **English (73.50)** | Weakest: **Physics (67.65)**
- Best department: **CSE (84.23 average)**
- 5 students have attendance shortage (< 75%)

Screenshots:

![Program output screenshot 1](Output_Screenshot/Screenshot%202026-10-27%20132808.png)
![Program output screenshot 2](Output_Screenshot/Screenshot%202026-10-27%20132827.png)
![Program output screenshot 3](Output_Screenshot/Screenshot%202026-10-27%20132844.png)

## 8. Final Outcome
The system reads student data, computes totals, averages, grades and pass/fail status, and produces subject-wise, department-wise and top-performer analysis in a clear console report, meeting all required features of the assignment.

## 9. Challenges & Learning
It covers four challenges (the pass rule, moving between Pandas and NumPy, department stats with groupby, hard-coded values) and three things learned about functions, loops versus NumPy/Pandas, and documentation.
- Defining the pass rule: My first idea was to pass students on their average marks, but that would let a student with 20 in one subject pass. I changed the rule so a student must score at least 35 in every subject, and used np.all() to check all five subjects at once.
- Moving between Pandas and NumPy: I was unsure how to apply NumPy functions to DataFrame data. I learned that df[SUBJECTS].to_numpy() converts the marks into an array, so np.sum(..., axis=1) and np.mean(..., axis=1) work row by row.
- Department-wise statistics: Doing this with loops was long and messy. Using groupby() with agg() gave the student count, average marks and pass count per department in a few lines.
- Hard-coded values: Grade limits, the pass mark and the attendance limit were first written inside the logic. I moved them to constants (PASS_MARK, MIN_ATTENDANCE) so they can be changed in one place.

## 10. GitHub Repository
https://github.com/Himmu725/Student_Performance_Analytics

## How to Run
```bash
pip install -r requirements.txt
python main.py
```

## Project Structure
```
student-performance-analytics/
├── main.py            # runs the analysis and prints the report
├── functions.py       # reusable calculation/processing functions
├── students.csv       # dataset (20 records)
├── results.csv        # generated processed output
├── output.txt         # sample program output
├── requirements.txt
└── README.md          # project documentation
```
