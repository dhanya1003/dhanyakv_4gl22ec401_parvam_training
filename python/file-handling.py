#creating a file using open method with 'x' mode, if the file already exits then it throws an error
# with open("new_file.txt", "x") as f:
#     f.write("Newly created the text file using python with 'x' mode.")

#x-create, a-append, w-write, r-read

#Overwrite the file if it already exists without any error, if not then create a new file
with open("new_file.txt", "w") as f:
    f.write("The text file created using python with 'w' mode.")

#Overwrite the file or update if it already exists without any error, if not then create a new file
with open("new_file.txt", "a") as f:
    f.write("\nThe new text has been added or appened using 'a' mode.")

#writing the content in a file
with open("new_file.txt", "w") as f:
    f.write("This is the first sentence.\n")
    f.write("This is the second sentence.")

#reading the content in a file
with open("new_file.txt", "r") as f:
    for line in f:
        print(line.strip())
    print(type(line.strip()))

#reading the content from a file and make it as a list using readlines method
with open("new_file.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    print(type(lines))

#reading the content from a file and make it as a list using readlines method for first line
with open("new_file.txt", "r") as f:
    line = f.readline()
    print(line)
    print(type(line))

#renaming a file
# import os
# os.rename("new_file.txt", "sample_file.txt")
# print("File renamed from new_file.txt to sample_file.txt")

#check whether the file is opened or closed
file = open("sample_file.txt", "r")
print("File is closed?", file.closed)
file.close()
print("File is closed?", file.closed)

#deleting a file
import os
if os.path.exists("sample_file.txt"):
    os.remove("sample_file.txt")
    print("The file has been deleted!")
else:
    print("The file has not deleted!")