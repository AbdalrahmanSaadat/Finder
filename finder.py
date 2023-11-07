#basic guidelines for using
print("!!!_____Enter the file name first, when finish type done_____!!!")

#input of the file name
inp_1=input("Enter file name:\n")

# handle the file
try:
    fhand = open(inp_1)

except:
    print("Try another file!")
    quit()


#work on counting function