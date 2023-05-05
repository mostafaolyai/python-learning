from pathlib import Path
from zipfile import ZipFile

# with ZipFile('files.zip', 'w') as zip:
#     for path in Path().rglob('*.*'):
#         zip.write(path)

with ZipFile('files.zip') as zip:
    print(zip.namelist())
    print(zip.getinfo(zip.namelist()[2]))
    zip.extractall('extracted')
