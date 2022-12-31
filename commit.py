import os
import subprocess
from datetime import datetime, timedelta

# Set up the GitHub repo location
repo_dir = r"E:\\PUNYA PROJECTS\\commit-art\\github-commit-art"  # raw string avoids escape issues
os.chdir(repo_dir)

# Define the commit message art and days between commits
letters = ['B', 'I', 'T', 'C', 'H', ' ', 'P', 'L', 'Z']
start_date = datetime(2023, 1, 1)

# Function to create and commit each change
def create_commit(letter, commit_date):
    filename = "commit_art.txt"
    
    # Write the letter to the file
    with open(filename, "w") as file:
        file.write(letter)
    
    # Format the commit date (with timezone)
    date_str = commit_date.strftime('%Y-%m-%dT%H:%M:%S') + '+0530'  # IST timezone
    
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    # Add and commit with a unique message
    subprocess.run(['git', 'add', filename], check=True)
    subprocess.run(['git', 'commit', '-m', f"Adding letter '{letter}' on {commit_date.strftime('%Y-%m-%d')}"], env=env, check=True)

# Commit each letter
for i, letter in enumerate(letters):
    commit_date = start_date + timedelta(days=i)
    create_commit(letter, commit_date)

# Push once at the end
subprocess.run(['git', 'push', '-u', 'origin', 'main'])

print("✅ Completed committing the phrase 'BITCH PLZ'!")
