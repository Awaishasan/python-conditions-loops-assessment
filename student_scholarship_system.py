# Student Scholarship Eligibility System
# Topic: Conditional Statements (if, elif, else)
# Assignment 47 - Task 1
# Checks a student for a scholarship using marks, attendance
# and monthly family income.


def get_student_name():
    """Ask for the student's name until a non-empty name is given."""
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please enter a valid name.")


def get_marks():
    """Ask for academic marks (0 to 100) with validation."""
    while True:
        try:
            marks = float(input("Enter academic marks (0 - 100): "))
            if 0 <= marks <= 100:
                return marks
            print("Invalid marks. Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number for marks.")


def get_attendance():
    """Ask for attendance percentage (0 to 100) with validation."""
    while True:
        try:
            attendance = float(
                input("Enter attendance percentage (0 - 100): "))
            if 0 <= attendance <= 100:
                return attendance
            print("Invalid attendance. Attendance must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number for attendance.")


def get_family_income():
    """Ask for monthly family income (Rs. 0 or more) with validation."""
    while True:
        try:
            income = float(input("Enter monthly family income (Rs.): "))
            if income >= 0:
                return income
            print("Invalid income. Income cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a number for income.")


def main():
    print("=" * 50)
    print("Student Scholarship Eligibility System")
    print("=" * 50)

    # Step 1: Collect student information
    student_name = get_student_name()
    marks = get_marks()
    attendance = get_attendance()
    family_income = get_family_income()

    # Step 2: Apply the eligibility criteria and collect
    # every reason for ineligibility, so the student can
    # see exactly which condition was not met.
    reasons = []

    if marks < 80:
        reasons.append("Academic marks are below 80%")
    if attendance < 85:
        reasons.append("Attendance is below 85%")
    if family_income > 50000:
        reasons.append("Monthly family income is above Rs. 50,000")

    # Step 3: Decide the scholarship type.
    # Full Scholarship: marks 90% or above
    # Partial Scholarship: marks 80% to 89%
    # Both need all three conditions above to be satisfied.
    scholarship_type = "Not Eligible"
    if not reasons:
        if marks >= 90:
            scholarship_type = "Full Scholarship"
        elif marks >= 80:
            scholarship_type = "Partial Scholarship"

    # Step 4: Display a complete scholarship evaluation report
    print("\n" + "=" * 50)
    print("Scholarship Evaluation Report")
    print("=" * 50)
    print(f"Student Name           : {student_name}")
    print(f"Academic Marks         : {marks}%")
    print(f"Attendance             : {attendance}%")
    print(f"Monthly Family Income  : Rs. {family_income:,.2f}")
    print("-" * 50)

    if scholarship_type == "Not Eligible":
        print("Eligibility Status     : Not Eligible")
        print("Scholarship Awarded    : None")
        print("\nReason(s) for Ineligibility:")
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("Eligibility Status     : Eligible")
        print(f"Scholarship Awarded    : {scholarship_type}")

    print("=" * 50)


if __name__ == "__main__":
    main()
