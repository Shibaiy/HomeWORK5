import os
import zipfile
from pathlib import Path


list_files=[]
directory = os.getcwd() + str(Path('/tmp'))
for i in os.listdir(directory):
    list_files.append(str(Path('.')) + str(Path('/tmp/')) + str(Path('/'))  + i)
print(list_files)

archive = str(Path('./tmp/test_archive.zip'))
with zipfile.ZipFile(archive,"w") as test_archive:
    for file in list_files:
        test_archive.write(file)
