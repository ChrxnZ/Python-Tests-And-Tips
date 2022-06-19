import os

files = [] #  Defining "Files" As A Variable To Store Files For Encryption

for file in os.listdir(): #  Basically Saying: "For Files In Script Directory"
  if file == "FindFilesInScriptDirectory.py": #  If File In Script Directory = "This_Script_Name.py" Then:
    continue #  Ignore
  if os.path.isfile(file): #  If Files In Script Directory = A File (Not Directory Or Folder) Then: 
    files.append(file) #  Send All File Names To List Defined By "files"
print("Found Files: ")
print(files)
