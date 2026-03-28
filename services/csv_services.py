from pathlib import Path

base = Path(__file__).parent
path = base /"coders.csv"
file_exists = path.exists()

