file=open('codingal.txt','r')
print(file.read())
file.close()

file=open('codingal.txt','r')
print(file.read(8))
file.close()

file=open('codingal.txt','a')
file.write(" Hi, my name is Maham")
file.close()