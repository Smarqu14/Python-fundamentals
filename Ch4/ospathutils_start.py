#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    # print(os.name)
    # Check for item existence and type
    # print("Item exists: " + str(path.exists("myfile.txt")))
    # print("Item is a file: " + str(path.isfile("myfile.txt")))
    # print("Item is a directory: " + str(path.isdir("myfile.txt")))

    # Work with file paths
    # print("item path: " + str(path.realpath("myfile.txt")))
    # print("Item path and name:" + str(path.split(path.realpath("myfile.txt"))))

    # Get the modification time
    t = time.ctime(path.getmtime("myfile.txt"))
    # print(t)
    # print(datetime.datetime.fromtimestamp(path.getmtime("myfile.txt")))
    # Calculate how long ago t he item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime('myfile.txt'))
    print('it has been' + str(td) + 'since the file was modified')
    print("or," + str(td.total_seconds()) + "second")


if __name__ == "__main__":
    main()
