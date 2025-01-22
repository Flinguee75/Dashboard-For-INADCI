import os

from dashboard.config import BASE_DIR

IA_path = os.path.join(BASE_DIR, "ia")
print("IA path exists:", os.path.exists(IA_path))

if os.path.exists(IA_path):
    print("Contents of IA path:", os.listdir(IA_path))
else:
    print("IA path does not exist.")
paths = [os.path.join(IA_path, item) for item in os.listdir(IA_path)] if os.path.exists(IA_path) else []
print("Paths stored:", paths)
