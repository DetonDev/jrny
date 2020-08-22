#!/usr/bin/python3

"""

88888888  8888888b.   888b    888 Y88b   d88P
    "88b  888   Y88b  8888b   888  Y88b d88P
     888  888    888  88888b  888   Y88o88P
     888  888   d88P  888Y88b 888    Y888P
     888  8888888P"   888 Y88b888     888
     888  888 T88b    888  Y88888     888
     888  888  T88b   888   Y8888     888
     888  888   T88b  888    Y888     888
   .d88P 
 .d88P"   a command-line based journal
888P"     by Samuel Giles, licensed under GPL-3.0 

"""

# import needed modules
import argparse
import status
import write

# set up the parser
parser = argparse.ArgumentParser(
    prog="jrny", 
    description="JRNY: a command-line based journal")

group = parser.add_mutually_exclusive_group()

# add all arguments
group.add_argument(
    "-w", "--write", 
    action="store_true", 
    help="open journal entry for current date")

group.add_argument(
    "-s", "--status", 
    action="store_true", 
    help="get the current status of your journal")

arglist = parser.parse_args()

def main(args):
    
    """ select appropriate response """
    
    if args.status == True:
        status.status()

    elif args.write == True:
        write.write()

    else:
        parser.print_help()

if __name__ == "__main__":
    main(arglist)
