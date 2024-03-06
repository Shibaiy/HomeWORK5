import os
import zipfile
from pathlib import Path
import variables as v


list_files=[]
for i in os.listdir(v.download_default_directory):
    list_files.append(v.default_directory + i)



with zipfile.ZipFile(v.archive,"w") as test_archive:
    for file in list_files:
        test_archive.write(file)
