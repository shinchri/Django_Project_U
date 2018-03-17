# open file and write to it ('w')
fw = open('sample.txt', 'w')

fw.write("Writing some stuff in my text file\n")
fw.write("I like bacon\n")

fw.close()

# read file
fr = open('sample.txt', 'r')

# reads all the content
# returns each line as a list
text = fr.readlines()

# strip any '\n' from the list
lines = [line.rstrip('\n') for line in text]

print(text)
print(lines)
fr.close()
