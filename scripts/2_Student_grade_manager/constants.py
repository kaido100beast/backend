from pathlib import Path
BASE_DIR = Path(__file__).parent
JSON_PATH = BASE_DIR / "students.json"
MENU = '''
Welcome to the students Grade Manager!
        1. Add students
        2. Delete students
        3. update students
        4. search students
        5. View students
        6. Highest Scorer
        7. Save Data
        8. Exit
Please select an option (1-8): '''