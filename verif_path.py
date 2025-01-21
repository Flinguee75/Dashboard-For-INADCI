import os

from dashboard.config import BASE_DIR

IA_path = os.path.join(BASE_DIR, "IA")
print("IA path exists:", os.path.exists(IA_path))

for key, path in paths.items():
    print(f"{key} exists:", os.path.isfile(path))
