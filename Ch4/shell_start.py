#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive  # this module makes it possible to zip files
# if you want to be more specific when making a zip file import zipfile module
from zipfile import ZipFile


def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):  # tomake sure the file exists
      # get the path to the file in the current directory
        src = path.realpath("myfile.txt")
      # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"
      # copy over the permissions, modification times, and other info
        # shutil.copy(src, dst)
        # shutil.copystat(src, dst)
      # rename the original file
        # os.rename("myfile.txt", "newname.txt")

      # now put things into a ZIP archive
        # root_dir, tail = path.split(src)
        # shutil.make_archive("archive", "zip")
      # more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("myfile.txt")
            newzip.write("myfile.txt.bak")


if __name__ == "__main__":
    main()
