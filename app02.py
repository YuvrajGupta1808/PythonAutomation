import os
import shutil

def sort_files_by_type(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The specified directory {directory} does not exist.")
        return

    # List all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # If it's a file, not a directory
        if os.path.isfile(file_path):
            # Extract the file extension (without the dot)
            file_extension = os.path.splitext(filename)[1][1:]

            # If no extension, classify as "Other"
            if not file_extension:
                file_extension = "Other"

            # Create the directory for the file type, if it doesn't exist
            extension_dir_path = os.path.join(directory, file_extension)
            if not os.path.exists(extension_dir_path):
                os.makedirs(extension_dir_path)

            # Move the file to the respective directory
            shutil.move(file_path, os.path.join(extension_dir_path, filename))
    
    print(f"Sorted all files in {directory} by file type.")

if __name__ == "__main__":
    dir_to_sort = input("Enter the directory you want to sort: ").strip()
    sort_files_by_type(dir_to_sort)
