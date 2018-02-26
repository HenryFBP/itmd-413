'''
Checking Path Validity
Many Python functions will crash with an error if you supply them with a path that does not exist.
The os.path module provides functions to check whether a given path exists and whether it is a file or folder.

Calling os.path.exists(path) will return True if the file or folder referred to in the argument exists and will
return False if it does not exist.

Calling os.path.isfile(path) will return True if the path argument exists and is a file and will return False otherwise.

Calling os.path.isdir(path) will return True if the path argument exists and is a folder and will return False otherwise.

'''
import os
'''windows examples'''
#print (os.path.exists('C:\\Windows'))
#print(os.path.isdir('C:\\Windows\\System32'))
#print(os.path.isfile('C:\\Windows\\System32'))

#File employees.txt check
print(os.path.exists("employees.txt"))
