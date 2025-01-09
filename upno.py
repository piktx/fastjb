import os
import random
import subprocess
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def read_number():
    try:
        with open('number.txt', 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        logging.warning("Number file not found. Starting from 0.")
        return 0

def write_number(num):
    try:
        with open('number.txt', 'w') as f:
            f.write(str(num))
        logging.info(f"Updated number to: {num}")
    except IOError as e:
        logging.error(f"Error writing number: {e}")
        raise

def git_commit_and_push():
    try:
        # Stage, commit, and push
        subprocess.run(['git', 'add', 'number.txt'], check=True)
        commit_message = f"Update number: {datetime.now().strftime('%Y-%m-%d')}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        subprocess.run(['git', 'push'], check=True)
        
        logging.info("Successfully committed and pushed changes")
    except subprocess.CalledProcessError as e:
        logging.error(f"Git operation failed: {e}")
        raise

def main():
    try:
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)
        git_commit_and_push()
    except Exception as e:
        logging.error(f"Script failed: {e}")
        exit(1)

if __name__ == "__main__":
    main()
