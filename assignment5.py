with open('sample.txt', 'r') as f:
    line=f.read()

print("Lines in sample.txt:")
print(line)


with open('sample.txt','w') as f:
    f.write("This is 1st line added to sample.txt \n")
    f.write("This is 2nd line added to sample.txt \n")
    f.write("This is 3rd line added to sample.txt \n")


with open('sample.txt','a') as f:
    f.write("This is appended line \n")
    f.write("This is 2nd appended line  \n")
    f.write("This is 3rd appended line \n")



