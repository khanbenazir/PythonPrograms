
# To write
f = open("textfile.txt", 'w+')    # 'w' followed by a '+' means it writes to an existing file
f.write("hello world")             #  or creates a new one if it doesn't exist
f.close()

# It overwrites the existing content
f = open("textfile.txt", 'w')
for i in range(1, 6):
    f.write("This is line " + str(i) + "\n")
f.close()

# If we want to new content to existing content
f = open("textfile.txt", 'a')
f.write("This is a new line. ")
f.close()

# If we want to only read a file
f = open("textfile.txt", 'r')
contents = f.read()
print(contents)

# If we want to read a file line by line
f = open("textfile.txt", 'r')
lines = f.readlines()
for i in lines:
    print(i)
f.close()

# To read first line of the file
f = open("textfile.txt", 'r')
rl = f.readline()
print(rl)
f.close()
