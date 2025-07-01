import sys
import os

STORAGE_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.env")

class Storage:
    def __init__(self):
        self.filepath = STORAGE_FILE_PATH

    def get(self, key):
        try:
            with open(self.filepath, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith(f"{key}="):
                        return line.split("=", 1)[1]
        except FileNotFoundError:
            pass
        return None

    def set(self, key, value):
        updated = False
        lines = []

        try:
            with open(self.filepath, 'r') as file:
                for line in file:
                    if line.startswith(f"{key}="):
                        lines.append(f"{key}={value}\n")
                        updated = True
                    else:
                        lines.append(line)
        except FileNotFoundError:
            pass

        if not updated:
            lines.append(f"{key}={value}\n")

        with open(self.filepath, 'w') as file:
            file.writelines(lines)