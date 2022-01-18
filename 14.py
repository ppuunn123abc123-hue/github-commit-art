import os
import subprocess
from datetime import datetime, timedelta

# Your input data
coordinates = [
    {"x": 2, "y": 2}, {"x": 2, "y": 3}, {"x": 2, "y": 4}, {"x": 2, "y": 5}, {"x": 2, "y": 6},
    {"x": 3, "y": 4}, {"x": 4, "y": 2}, {"x": 4, "y": 3}, {"x": 4, "y": 4}, {"x": 4, "y": 5},
    {"x": 4, "y": 6}, {"x": 6, "y": 3}, {"x": 6, "y": 4}, {"x": 6, "y": 5}, {"x": 6, "y": 6},
    {"x": 7, "y": 2}, {"x": 7, "y": 5}, {"x": 8, "y": 3}, {"x": 8, "y": 4}, {"x": 8, "y": 5},
    {"x": 8, "y": 6}, {"x": 10, "y": 2}, {"x": 10, "y": 3}, {"x": 10, "y": 4}, {"x": 10, "y": 5},
    {"x": 10, "y": 6}, {"x": 11, "y": 2}, {"x": 11, "y": 4}, {"x": 12, "y": 3}, {"x": 14, "y": 2},
    {"x": 14, "y": 3}, {"x": 14, "y": 4}, {"x": 14, "y": 5}, {"x": 14, "y": 6}, {"x": 15, "y": 2},
    {"x": 15, "y": 4}, {"x": 16, "y": 3}, {"x": 18, "y": 2}, {"x": 18, "y": 3}, {"x": 19, "y": 4},
    {"x": 19, "y": 5}, {"x": 19, "y": 6}, {"x": 20, "y": 2}, {"x": 20, "y": 3}, {"x": 24, "y": 3},
    {"x": 24, "y": 6}, {"x": 25, "y": 2}, {"x": 25, "y": 5}, {"x": 25, "y": 6}, {"x": 26, "y": 2},
    {"x": 26, "y": 4}, {"x": 26, "y": 6}, {"x": 27, "y": 3}, {"x": 27, "y": 6}, {"x": 29, "y": 3},
    {"x": 29, "y": 4}, {"x": 29, "y": 5}, {"x": 30, "y": 2}, {"x": 30, "y": 6}, {"x": 31, "y": 3},
    {"x": 31, "y": 4}, {"x": 31, "y": 5}, {"x": 33, "y": 4}, {"x": 33, "y": 6}, {"x": 34, "y": 2},
    {"x": 34, "y": 3}, {"x": 34, "y": 4}, {"x": 34, "y": 5}, {"x": 34, "y": 6}, {"x": 35, "y": 6},
    {"x": 37, "y": 2}, {"x": 37, "y": 3}, {"x": 37, "y": 4}, {"x": 38, "y": 4}, {"x": 39, "y": 2},
    {"x": 39, "y": 3}, {"x": 39, "y": 4}, {"x": 39, "y": 5}, {"x": 39, "y": 6}, {"x": 42, "y": 2},
    {"x": 42, "y": 3}, {"x": 42, "y": 4}, {"x": 42, "y": 6}, {"x": 44, "y": 4}, {"x": 45, "y": 5},
    {"x": 46, "y": 2}, {"x": 46, "y": 3}, {"x": 46, "y": 5}, {"x": 46, "y": 6}, {"x": 47, "y": 2},
    {"x": 47, "y": 3}, {"x": 47, "y": 5}, {"x": 47, "y": 6}, {"x": 48, "y": 5}, {"x": 48, "y": 6},
    {"x": 49, "y": 2}, {"x": 49, "y": 3}, {"x": 49, "y": 5}, {"x": 49, "y": 6}, {"x": 50, "y": 2},
    {"x": 50, "y": 3}, {"x": 50, "y": 5}, {"x": 50, "y": 6}, {"x": 51, "y": 5}, {"x": 52, "y": 4}
]

commits_per_day = 60

# Start date of the graph (53 weeks ago, Sunday)
start_date = datetime.today() - timedelta(weeks=52)
start_date -= timedelta(days=start_date.weekday() + 1)  # Go back to last Sunday

for point in coordinates:
    x, y = point['x'], point['y']
    commit_date = start_date + timedelta(weeks=x, days=y)
    for i in range(commits_per_day):
        with open("commit.txt", "a") as file:
            file.write(f"Commit on {commit_date} - {i}\n")
        env = os.environ.copy()
        date_str = commit_date.strftime('%Y-%m-%dT12:00:00')
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        subprocess.run(["git", "add", "commit.txt"], env=env)
        subprocess.run(["git", "commit", "-m", f"Commit on {commit_date} #{i}"], env=env)

print("Done generating commits!")
