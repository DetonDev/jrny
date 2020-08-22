#!/usr/bin/python3

"""

JRNY/status.py

print the status message from "jrny -s"

"""

# import needed modules
import variables
import os

def status():

    if os.path.exists(variables.current_directory + variables.current_filename):
        print("\n[✔] Journal entry found for " + variables.time_full)
    else:
        print("\n[✘] No journal entry for " + variables.time_full)

    NOF = 0

    for root, dirs, files in os.walk(variables.rootdir, topdown=False):
        for name in files:
            NOF += 1

    print("\n[?] Total entries: " + str(NOF) +
          "\n    Journal location: " + variables.rootdir +
          "\n    Entry format: ." + variables.filetype)
