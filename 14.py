import os
import subprocess
from datetime import datetime, timedelta

# 7x5 pixel block font (uppercase only)
FONT = {
    "A": [
        "01110",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
    ],
    "B": [
        "11110",
        "10001",
        "10001",
        "11110",
        "10001",
        "10001",
        "11110",
    ],
    "C": [
        "01111",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "01111",
    ],
    "H": [
        "10001",
        "10001",
        "10001",
        "11111",
        "10001",
        "10001",
        "10001",
    ],
    "I": [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
        "11111",
    ],
    "L": [
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111",
    ],
    "P": [
        "11110",
        "10001",
        "10001",
        "11110",
        "10000",
        "10000",
        "10000",
    ],
    "T": [
        "11111",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
        "00100",
    ],
    "Z": [
        "11111",
        "00001",
        "00010",
        "00100",
        "01000",
        "10000",
        "11111",
    ],
}

TEXT = "BITCH PLZ"
COMMITS_PER_PIXEL = 50
START_DATE = datetime(2021, 1, 3)  # First Sunday of 2021

def generate_coordinates(text):
    coords = []
    x_offset = 0
    for char in text.upper():
        if char == " ":
            x_offset += 3  # space between words
            continue
        pattern = FONT.get(char)
        if not pattern:
            x_offset += 6
            continue
        for y, row in enumerate(pattern):
            for x, val in enumerate(row):
                if val == "1":
                    coords.append({"x": x + x_offset, "y": y})
        x_offset += 6  # 5 width + 1 space
    return coords

def main():
    coords = generate_coordinates(TEXT)
    total = len(coords) * COMMITS_PER_PIXEL
    print(f"🧱 Generating ~{total} commits for '{TEXT}' in 2021...")

    for point in coords:
        week = point["x"]
        day = point["y"]
        commit_date = START_DATE + timedelta(weeks=week, days=day)
        for i in range(COMMITS_PER_PIXEL):
            env = os.environ.copy()
            date_str = commit_date.strftime("%Y-%m-%dT12:00:00")
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str
            subprocess.run([
                "git", "commit", "--allow-empty",
                "-m", f"{TEXT} pixel ({week},{day}) commit #{i}"
            ], env=env)

    print("✅ Done! Push to GitHub and your 2021 graph will display 'BITCH PLZ'.")

if __name__ == "__main__":
    main()
