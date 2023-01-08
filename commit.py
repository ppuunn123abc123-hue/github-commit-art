import os
import subprocess
from datetime import datetime, timedelta

# Set up the GitHub repo location
repo_dir = r"E:\\PUNYA PROJECTS\\commit-art\\github-commit-art"  # raw string avoids escape issues
os.chdir(repo_dir)
# Define the commit message art and days between commits
letters = ['B', 'I', 'T', 'C', 'H', ' ', 'P', 'L', 'Z']  # The phrase
commit_dates = []
start_date = datetime(2023, 1, 1)  # Start date for the first commit (Change if needed)

# Create a list of commit dates (one per day)
for i in range(len(letters)):
    commit_dates.append(start_date + timedelta(days=i))

# Function to create and commit each change
def create_commit(letter, commit_date):
    # Create a dummy file with the letter
    filename = "commit_art.txt"
    with open(filename, "w") as file:
        file.write(letter)  # Write the letter to the file
    
    # Stage the file and commit it with a specific date
    subprocess.run(['git', 'add', filename])
    commit_message = f"Adding letter {letter} to commit art"
    subprocess.run([
        'git', 'commit', '--amend', '--no-edit', '--date', commit_date.strftime('%a %b %d %H:%M:%S %Y %z')
    ])

    # Push the commit (this assumes you have a remote setup)
    subprocess.run(['git', 'push'])

# Commit each letter
for i, letter in enumerate(letters):
    create_commit(letter, commit_dates[i])

print("Completed committing the phrase 'BITCH PLZ'!")