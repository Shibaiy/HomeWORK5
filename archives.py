import os
import zipfile
from zipfile import ZipFile
from pathlib import Path


list_files=[]
directory = os.getcwd() + str(Path('/tmp'))
print(list_files)
for i in os.listdir(directory):
    list_files.append(directory + str(Path('/')) + i)
print(list_files)

archive = "test_archive.zip"
with zipfile.ZipFile(archive,"w") as test_archive:
    for file in list_files:
        test_archive.write(file)
