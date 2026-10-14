# Project Documentation
## Student Performance Analytics System

**Submitted by:** Sarvesh Singh  
**Course:** Python with AI  
**Institute:** United Institute of Technology, Allahabad  
**Technologies:** Python, Pandas, NumPy, CSV  
**Project type:** Beginner-level data analysis

## 1. Introduction
The Student Performance Analytics System reads student records from a CSV file and performs basic academic analysis. It calculates totals and averages, assigns grades, determines pass/fail status, finds the highest and lowest totals, displays the top three students, calculates subject-wise averages, and saves the processed data.

This project demonstrates Python fundamentals and data analysis. It does not train a machine-learning model.

## 2. Objectives
- Read student records from `students.csv`.
- Calculate total and average marks for five subjects.
- Assign grades using a reusable function.
- Determine pass/fail status using marks and attendance.
- Identify highest-scoring and lowest-scoring students.
- Display the top three students by total marks.
- Calculate average marks for each subject.
- Export the processed dataset to `result.csv`.

## 3. Technologies Used
- **Python:** Main programming language, loops, conditions and functions.
- **Pandas:** Reads and manages CSV data, selects columns, sorts records and writes output.
- **NumPy:** Calculates totals, averages and minimum subject marks.
- **CSV:** Stores input data and processed output.

## 4. Dataset Description
The input file `students.csv` contains 20 student records. Columns are:
- `Student_ID`: student identifier
- `Name`: student name
- `Department`: department name
- `Python`, `Mathematics`, `AI`, `Data Analysis`, `English`: marks in five subjects
- `Attendance`: attendance percentage

The marks are on a 0–100 scale. Column names in the CSV must match those used in `main.py`.

## 5. Project Files
| File | Description |
|---|---|
| `main.py` | Loads data, performs calculations and prints analysis |
| `functions.py` | Contains the `get_grade()` function |
| `students.csv` | Input dataset with 20 student records |
| `requirements.txt` | Lists Pandas and NumPy |
| `README.md` | Project overview and run instructions |
| `Project_Documentation.md` | Editable project documentation |
| `Project_Documentation.pdf` | Printable version of the documentation |
| `RUN_INSTRUCTIONS.txt` | Quick run instructions |
| `result.csv` | Generated processed dataset; recreated each time the program runs |

## 6. Implementation
1. Import Pandas and NumPy, then import `get_grade()` from `functions.py`.
2. Read `students.csv` into a Pandas DataFrame.
3. Select the five subject columns and convert them into a NumPy array.
4. Use NumPy to calculate row-wise totals and averages.
5. Use a loop to assign a grade and determine each student's result.
6. Print the student table, highest and lowest total, and top three students.
7. Calculate the average marks for each subject.
8. Save the final DataFrame to `result.csv`.

## 7. Calculation Rules
### Total marks
Sum of marks in Python, Mathematics, AI, Data Analysis and English.

### Average marks
Total marks divided by five subjects, rounded to two decimal places.

### Grade rule
| Average | Grade |
|---:|---|
| 90 or above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | F |

### Pass/fail rule
A student is marked **Pass** if the minimum mark across all five subjects is at least 40 and attendance is at least 75%. Otherwise, the result is **Fail**.

## 8. Key Features
- Student-wise marks summary
- Highest and lowest total marks
- Top three students sorted by total marks
- Pass/fail counts
- Subject-wise average marks
- CSV export of calculated results

## 9. Output and Results
When the program runs, it displays:
- Student result table
- Highest marks and student name
- Lowest marks and student name
- Top three students
- Total, passed and failed student counts
- Subject-wise averages

The generated `result.csv` contains the original input fields plus `Total`, `Average`, `Grade` and `Result`.

**Important:** The exact values shown in the terminal depend on the current contents of `students.csv`. Run the current program and use your actual terminal output for screenshots. Do not use a screenshot from a different code/data version.

### Screenshots to add before submission
1. Terminal showing the student result table.
2. Terminal showing highest/lowest marks and top three students.
3. Terminal showing class summary and subject averages.
4. `result.csv` opened in VS Code or a spreadsheet.

## 10. How to Run
1. Install Python 3.
2. Open Terminal in the project folder.
3. Install packages:
   `python3 -m pip install -r requirements.txt`
4. Run:
   `python3 main.py`
5. Check the terminal output and open `result.csv`.

Keep `main.py`, `functions.py` and `students.csv` in the same folder.

## 11. Challenges and Learning
This project provides practice in:
- Reading CSV data with Pandas
- Selecting DataFrame columns
- Using NumPy arrays for calculations
- Writing functions, loops and `if-else` conditions
- Sorting and filtering student records
- Exporting processed data to a CSV file

If an error occurs, first check that the required packages are installed and that the CSV column names match the names used in the program.

## 12. Limitations
- The input CSV must contain the expected columns and numeric values.
- The pass/fail thresholds are fixed at 40 marks in every subject and 75% attendance.
- This project summarizes data; it does not predict student performance with machine learning.
- Results change if the input data changes.

## 13. Conclusion
The project demonstrates how Python, Pandas and NumPy can be used to analyze student marks. It produces student-wise totals and averages, grades, pass/fail results, top performers, subject averages and a processed CSV output.

## 14. GitHub Repository
**Repository URL:** Add your actual GitHub repository URL here before submission.

## 15. References
- Python documentation: https://docs.python.org/3/
- Pandas documentation: https://pandas.pydata.org/docs/
- NumPy documentation: https://numpy.org/doc/
- Project assignment PDF supplied for the Python with AI course.
