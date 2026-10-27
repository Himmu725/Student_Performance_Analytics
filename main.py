"""Student Performance Analytics System - main program."""
import functions as fn


def print_section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def main():
    # Step 1-2: load and inspect data
    df = fn.load_data("students.csv")
    print_section("1. DATASET OVERVIEW")
    print(f"Records: {df.shape[0]} | Columns: {df.shape[1]}")
    print("Columns:", ", ".join(df.columns))
    print("Missing values:", int(df.isnull().sum().sum()))
    print(df.head().to_string(index=False))

    # Step 3: process
    df = fn.calculate_total_and_average(df)
    df = fn.add_grades(df)
    df = fn.add_result_status(df)

    print_section("2. STUDENT RESULTS")
    cols = ["Student_ID", "Name", "Department", "Total", "Average",
            "Grade", "Result", "Attendance", "Attendance_Status"]
    print(df[cols].to_string(index=False))

    # Step 4: analysis
    print_section("3. CLASS SUMMARY")
    for key, value in fn.class_summary(df).items():
        print(f"{key:<22}: {value}")

    print_section("4. SUBJECT-WISE ANALYSIS")
    subject_df = fn.subject_analysis(df)
    print(subject_df.to_string(index=False))
    best = subject_df.loc[subject_df["Average"].idxmax(), "Subject"]
    weakest = subject_df.loc[subject_df["Average"].idxmin(), "Subject"]
    print(f"\nBest subject (highest average)  : {best}")
    print(f"Weakest subject (lowest average): {weakest}")

    print_section("5. DEPARTMENT-WISE ANALYSIS")
    print(fn.department_analysis(df).to_string(index=False))

    print_section("6. TOP 3 PERFORMERS")
    print(fn.top_performers(df, 3).to_string(index=False))

    print_section("7. GRADE DISTRIBUTION")
    print(df["Grade"].value_counts().sort_index().to_string())

    print_section("8. FAILED STUDENTS")
    failed = df[df["Result"] == "Fail"][["Student_ID", "Name", "Average"]]
    print(failed.to_string(index=False))

    # Save processed results
    df.to_csv("results.csv", index=False)
    print("\nProcessed data saved to results.csv")


if __name__ == "__main__":
    main()
