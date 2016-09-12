fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
mail = []
for line in fh:
	if line.startswith('From '):
		line = line.split()
		mail.append(line[1])
		
		count = count + 1

print mail
