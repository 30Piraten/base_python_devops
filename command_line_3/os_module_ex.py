import os

a1 = os.getcwd()
a2 = os.chdir("../automating-FS_2/")
a3 = os.getcwd()
a4 = os.environ.get("LOGLEVEL")
a5 = os.environ["LOGLEVEL"] = "DEBUG"
a6 = os.environ.get("LOGLEVEL")
a7 = os.getlogin()

print(a1)
print(a2)
print(a3)
