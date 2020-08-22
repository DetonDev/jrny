#!/usr/bin/python3

"""

JRNY/write.py

handle file operations of "jrny -w"

"""

# import needed modules
import variables
import os
import subprocess

def write():
    if os.path.exists(variables.current_directory):
        print('[!] Directory "' + variables.current_directory + '" detected.')
    else:
        print("\n[%] Attempting to create " + variables.current_directory + "...")
        os.makedirs(variables.current_directory, 0o700)
        print("[✔] Directory created successfully!")

    print("[%] Opening editor...")
    subprocess.run([variables.editor, variables.current_directory + variables.current_filename], check=True)
