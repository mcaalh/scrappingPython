name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lsth = []
h = {}
for line in handle:
    if line.startswith("From "):
        line = line.split()
        hours = line[5].split(':')[0]
        lsth.append(hours)
for hour in lsth:
    h[hour] = h.get(hour,0) + 1
for hr, nb in sorted(h.items()):
    print hr, nb
        