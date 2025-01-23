file1=open('codingal.txt','r')
file2=open('codingal2.txt','w')
for line in file1.readlines():
    if (line.startswith("Coding")):
        print(line)
        file2.write(line)
file1.close()
file2.close()