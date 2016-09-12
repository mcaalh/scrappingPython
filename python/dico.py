name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
maxiVal = None
maxKey = None
mails = []

for line in handle:
	if line.startswith('From '):
		line = line.split()
		mails.append(line[1])
        
for mail in mails:
    counts[mail] = counts.get(mail,0) + 1

for i, j in counts.items():
    if maxiVal == None or maxiVal < j:
        maxiVal = j
        maxiKey = i
print maxiKey, maxiVal