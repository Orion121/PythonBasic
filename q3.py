# 3. Write to a File
# Write a program to create a text file and write some content to it.
# Using file functions like write and open.

with open("sample.txt", "w") as file:
    file.write("This is a sample file.\nThis file contains text written by a Python program.")
print("Content written to sample.txt")
