# Student Performance Analytics

A beginner-level Python project using Pandas and NumPy to review student marks.

## Files
- `main.py`: reads the data and shows student results.
- `functions.py`: contains the simple grade function.
- `students.csv`: sample student data.
- `requirements.txt`: libraries needed to run the project.

## Run it
1. Open VS Code.
2. Install the libraries:

   `python3 -m pip install -r requirements.txt`

3. Run the program:

   `python3 main.py`

The program shows totals, averages, grades, pass/fail results and subject averages. It also saves a copy as `result.csv`.

A student passes when every subject mark is at least 40 and attendance is at least 75%.
