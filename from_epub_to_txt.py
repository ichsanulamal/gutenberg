import os
from epub2txt import epub2txt

# Folder Path
path = "C:\\Users\\ichsan\\Documents\\proj\\gitenberg\\books"
  
# Change the directory
os.chdir(path)
  
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".epub"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        res = epub2txt(file_path)
        
        file_path = file_path.replace("epub", "txt")
        with open(file_path, "w", encoding="utf-8") as file1:
            # Writing data to a file
            file1.write(res)


