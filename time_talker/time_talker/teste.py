import os
from pathlib import Path

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
BASE_DIR = Path(__file__).resolve().parent.parent
file_path = os.path.join(BASE_DIR, 'front\cu.html')

print(file_path)
