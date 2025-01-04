import os
do_not_include = ['antiprocrastination.txt']
file_header = """
! Title: All Alex-vasc's personal annoyances
! Expires: 5 days
! Description: This list contains the sites on most of others lists of Alex's repository
! except for anti-procrastination list 
! Homepage: https://github.com/alexandre-vasc/miscfilters
! License: https://github.com/alexandre-vasc/miscfilters/LICENSE
! This filterlist is compatible with uBlock Origin and Adguard.
"""

def merge_files(directory):
    merged_lines = set()
    print('preparing to merge', directory)
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt") and filename not in do_not_include:
            filepath = os.path.join(directory, filename)
            print('processing file ' + filepath)
            
            # Read lines from the file and add them to the set
            with open(filepath, "r") as file:
                lines = file.readlines()
                print('found ' + str(len(lines)) + ' lines')
                for line in lines:                    
                    if (not line.startswith('!')) and len(line) > 1:
                        merged_lines.add(line)

    # Write merged lines to a new file
    with open("merged_output.txt", "w") as merged_file:
        merged_file.write(file_header)
        for line in sorted(merged_lines):
            merged_file.write(line.strip() + '\n')

if __name__ == "__main__":
    merge_files(".")