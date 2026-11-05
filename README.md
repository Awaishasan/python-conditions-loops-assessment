# Python Programming Assessment – Conditions & Loops

Assignment 47 – PSEB Bootcamp Portal
Student: Muhammad Awais Hassan

## Files
- `student_scholarship_system.py` – Task 1: Student Scholarship Eligibility System (if / elif / else)
- `pharmacy_inventory_system.py` – Task 2: Smart Pharmacy Inventory & Sales Management System (for loop, range(), counters and accumulators)

## Task 1 – Scholarship Eligibility
Evaluates eligibility from academic marks, attendance percentage, and monthly family income.
- Marks at least 80%, attendance at least 85%, family income Rs. 50,000 or less.
- 90% or above: Full Scholarship. 80–89%: Partial Scholarship.
- Otherwise, lists every reason for ineligibility and shows a complete evaluation report.
- All inputs are validated (marks / attendance 0–100, income 0 or more).

## Task 2 – Pharmacy Inventory & Sales
- Asks how many medicines to process, then uses a `for` loop for each one.
- Collects medicine name, available stock, price per unit, and quantity sold.
- Checks stock before a sale, calculates the sale amount and remaining stock.
- Low-stock warning if remaining stock is below 10 units.
- Keeps total revenue with an accumulator and counts medicines needing restocking.
- Final report: total medicines processed, total revenue, medicines needing restocking.

## How to run
```bash
python3 student_scholarship_system.py
python3 pharmacy_inventory_system.py
```

## Note on portal submission
The TechDestination portal does not accept `.py` uploads, so the two Python files were also submitted as a ZIP containing the `.py` files.
