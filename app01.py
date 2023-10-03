import os
import shutil
from difflib import get_close_matches

def movefile(sourcefilename, sourcedirectory, destinationdirectory):
    # Expand the user's home directory if it's in the paths
    sourcedirectory = os.path.expanduser(sourcedirectory)
    destinationdirectory = os.path.expanduser(destinationdirectory)

    # Construct the full source filepath
    sourcefilepath = os.path.join(sourcedirectory, sourcefilename)

    # Check if the source file exists
    if os.path.isfile(sourcefilepath):
        destinationfilepath = os.path.join(destinationdirectory, sourcefilename)
        shutil.move(sourcefilepath, destinationfilepath)
        print(f"{sourcefilename} moved to {destinationdirectory}")
    
    else:
        # If file doesn't exist, provide suggestions using get_close_matches
        suggestions = get_close_matches(sourcefilename, os.listdir(sourcedirectory), n=3)
        
        if suggestions:
            print(f"Did you mean any of these files?")
            for s in suggestions:
                print(f"- {s}")
        else:
            print(f"File {sourcefilename} not found in {sourcedirectory} and no close matches were found.")

if __name__ == "__main__":
    filename = input("Enter the filename you wish to move: ")
    src_dir = input("Enter the directory where this file currently resides: ")
    dest_dir = input("Enter the destination directory: ")

    # Expand the user's home directory for destination directory
    dest_dir = os.path.expanduser(dest_dir)

    # Ensure the destination directory exists, if not, create it.
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    movefile(filename, src_dir, dest_dir)
