#--------------------------------------------------------basic guidelines for using-------------------------------------
print("!!!_____Enter the file name first, Type:1..for counting and Type:2..for searching _____!!!")

#----------------------------------------------------------input of the file name---------------------------------------
inp_1=input("Enter file name:\n")

#------------------------------------------------------------handle the file------------------------------------------
try:
    fhand = open(inp_1)
    l_fhand = list(fhand)
    inp_2=input("choose 1 or 2?\n")
    if inp_2 == "1":
#----------------------------------------------------work on counting function------------------------------------------------
        line_count = 0
        word_count = 0
        for l in l_fhand:
            l = l.rstrip()
            line_count += 1
            for w in l:
                word_count +=1
        print("Lines count:",line_count)
        print("Words count:",word_count)
        #--------------------------------------------------most repeated words feature---------------------------------------------------
        fhand = open(inp_1)
        rhand= fhand.read().split()
        counter={}
        for s in rhand:
            counter[s]=counter.get(s,0) + 1

        new_counter=list()
        for k, v in counter.items():
            new_counter.append((v, k))
        new_counter=sorted(new_counter,reverse=True)
        inp_3=input("How many words:")  
        number=int(inp_3)  
        print("Most reapeated words:",new_counter[:number])
# ----------------------------------------------------search for specific word count---------------------------------------------------------
    elif inp_2 == "2":
        inp_4=input("Enter the word:")
        fhand = open(inp_1)
        for w in fhand:
            if inp_4 in w:
                print("Here is the line:",w)

    else:
        print("Try again")

except:
    print("Try another file!")
    quit()