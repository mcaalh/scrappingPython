import re
fiche = raw_input("nom du fichier")
if len(fiche) < 1 : fiche = "regex_sum_42.txt"
handle = open(fiche)
lst = list()
for line in handle:
	line = line.rstrip()
	stuff = re.findall('([0-9]+)', line)
	for num in stuff:
		num = int(num)
		lst.append(num)
print sum(lst)

# import re
# print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )