#work on counting function
#file input
fhand = (open("test.txt"))
l_fhand = list(fhand)

#loop around the file
line_count = 0
word_count = 0

for l in l_fhand:
    l = l.rstrip()
    line_count += 1
    for w in l:
        word_count +=1

#output
print("Line count:",line_count)
print("Word count:",word_count)

