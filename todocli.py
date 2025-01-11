#!/usr/bin/env python3

import os

from src.storage import load_data, save_data
from src.display import display_data
from src.option import add_entry, remove_entry

DEFAULT_DATA_FILE = ".data/default.csv"
DEFAULT_DATA_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), DEFAULT_DATA_FILE)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('option', nargs='?', type=str, help="NULL | add | remove")
    parser.add_argument('args', nargs='?', type=str, help="additional arguments (e.g. index to remove)") 

    # parser.add_argument('--data-file', type=str, default=DEFAULT_DATA_FILE, help="path to data file")
    parser.add_argument('--sortby', type=str, default=None, help="priority | deadline")
    args = parser.parse_args()
    
    option = args.option
    # data_file = args.data_file
    data_file = DEFAULT_DATA_FILE
    sortby = args.sortby

    # if data file does not exist, create it
    if not os.path.isfile(data_file):
        with open(data_file, 'w') as f:
            f.write("content,priority,deadline,status\n")

    data = load_data(data_file, sortby)

    if args.option is None:
        display_data(data)
        save_data(data, data_file)
        exit(0)

    if option == "add":
        data = add_entry(data)
    elif option == "remove":
        data = remove_entry(data, index=args.args)

    else:
        # print help
        print(f"Invalid option: {option}")
        parser.print_help()
        exit(0)
    
    save_data(data, data_file)