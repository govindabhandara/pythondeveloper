import os
if os.path.exists("abc.txt"):
    os.remove("abc.txt")
else:
    print("file doesnot exist")