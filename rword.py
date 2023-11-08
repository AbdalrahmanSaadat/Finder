fhand = (open("test.txt"))
rhand= fhand.read().split()
counter={}
for s in rhand:
    counter[s]=counter.get(s,0) + 1

new_counter=list()
for k, v in counter.items():
    new_counter.append((v, k))
new_counter=sorted(new_counter,reverse=True)

print("Most reapeated words:",new_counter[:10])

