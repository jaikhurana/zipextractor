import os,zipfile
from pathlib import Path
p=Path.home()
examplezip=zipfile.ZipFile(p/'Documents/python_codes/zipextractor/file1.zip')
examplezip.extractall(p/'Documents/python_codes/zipextractor')
examplezip.close()