##Task 1##

# Did this the quick and dirty way, nothing fancy here.
# Created a new folder on the C drive, dumped all new folders/subfolders in there
# Created each individually, then had to remove each one-by-one because "rmdir"
# cannot remove folders with other stuff in it.


import os
path = "C:\Task_1_Folder"

os.mkdir(path)
os.mkdir(path + "/draft_code")
os.mkdir(path + "/draft_code/pending")
os.mkdir(path + "/draft_code/complete")
os.mkdir(path + "/includes")
os.mkdir(path + "/layouts")
os.mkdir(path + "/layouts/default")
os.mkdir(path + "/layouts/post")
os.mkdir(path + "/layouts/post/posted")
os.mkdir(path + "/site")

os.rmdir(path + "/site")
os.rmdir(path + "/layouts/post/posted")
os.rmdir(path + "/layouts/post")
os.rmdir(path + "/layouts/default")
os.rmdir(path + "/layouts")
os.rmdir(path + "/includes")
os.rmdir(path + "/draft_coding/complete")
os.rmdir(path + "/draft_coding/pending")
os.rmdir(path + "draft_code")
