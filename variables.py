#!/usr/bin/python3

"""

JRNY/variables.py

store important values

"""

# import needed modules
from datetime import date
import configparser
from xdg import XDG_CONFIG_HOME

today = date.today() # get current date

# create config variable and read config file
config = configparser.ConfigParser(interpolation=None)

try:
    config.read(str(XDG_CONFIG_HOME) + '/jrny/config.ini')

    # read settings from config file
    rootdir = config['cfg']['ROOT_DIRECTORY']
    dirstruct = config['cfg']['DIRECTORY_STRUCTURE']
    filetype = config['cfg']['FILE_TYPE']
    time = today.strftime(config['cfg']['TIME_FORMAT'])
    editor = config['cfg']['TEXT_EDITOR']

    # more useful values
    current_directory = rootdir + today.strftime(dirstruct)
    current_filename = time + "." + filetype
    time_full = today.strftime("%B %d, %Y.")

except:
    print("\n[!] ERROR: Before using JRNY, you must create a config file at" +
          "\n    " + str(XDG_CONFIG_HOME) + '/jrny/config.ini\n')

