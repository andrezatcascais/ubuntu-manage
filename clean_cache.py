#!/usr/bin/env python3

import os
import datetime

# Path to the log file
LOG_FILE = os.path.expanduser("~/cron_job.log")

# Function to log messages
def log(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def clear_all():
    """
    Clears RAM Cache/Buffer, Dentries, and Inodes.
    """
    log("Starting to clear RAM Cache and Buffers...")
    result = os.system("sync; echo 3 > /proc/sys/vm/drop_caches")
    if result == 0:
        log("RAM Cache cleared successfully.")
    else:
        log("Failed to clear RAM Cache.")

def clear_swap():
    """
    To clear the disk space consumed by SWAP.
    Make sure there is enough free RAM before running this! 
    Otherwise, the system may freeze due to resource starvation.

    Clears SWAP space.
    """
    log("Starting to clear SWAP...")
    result = os.system("swapoff -a && swapon -a")
    if result == 0:
        log("SWAP cleared successfully.")
    else:
        log("Failed to clear SWAP.")

def show_log():
    """
    Displays the log file content on the screen.
    """
    print("\n--- Log Output ---")
    with open(LOG_FILE, "r") as log_file:
        print(log_file.read())

if __name__ == "__main__":
    clear_all()
    clear_swap()
    log("Cleanup task completed.")
    show_log()  # Display log contents after execution