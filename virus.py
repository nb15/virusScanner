userFile = input("What file would you like me to open?: ")
fread = open(userFile, "r+")

if "virus" in userFile:
	print("This file contains a virus. Contact help immediatly.")
else:
	print("File {} is virus free.".format(userfile))

fread.close()