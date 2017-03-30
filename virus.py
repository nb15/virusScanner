
# Ask user what file they would like to scan
userFile = input("What file would you like me to open?: ")

# Open the file the user chooses and read into the file
fread = open(userFile, "r+")

if "virus" in userFile:
	print("This file contains a virus. Contact help immediatly.")
else:
	print("File {} is virus free.".format(userfile))

# Close the file
fread.close()