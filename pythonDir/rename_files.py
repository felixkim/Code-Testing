import os
def rename_files():
	# get file names from a folder
	#file_list = os.listdir(r"C:\OOP\prank")
	#print(file_list)
	#get current directory being worked on
	saved_path = os.getcwd()
	print("Current Working Directory is " + saved_path)	

	# changes directory so we can do stuff in that folder
	os.chdir(r"C:\OOP\prank")
	# for each file, rename filename
	for file_name in file_list:
		print("Old Name - " + file_name)
		print("New Name - " + file_name.translate(None,"0123456789"))
		os.rename(file_name, file_name.translate(None,"0123456789"))

	os.chdir(saved_path)
rename_file()
