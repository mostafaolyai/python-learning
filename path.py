from pathlib import Path

path1 = Path("C:\\Users\\smo_2")
path2 = Path(r"C:\Users\smo_2")  # raw path
path3 = Path()  # current root
path4 = Path()/Path('ecommerce/__init__')  # combine

print(path1.exists())
print(path1.is_dir())
print(path1.absolute())
print(path1.is_file())
print(path4.with_suffix('.exe'))  # change just ext
