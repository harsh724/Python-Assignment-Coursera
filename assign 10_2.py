

name = connection("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hourdict = dict()

for line in handle:
    if(line.startswith('From:')): continue
    elif(line.startswith('From')):
        mylst = line.split()
        timestamp = mylst[5]
        hour = timestamp.split(':')[0]
        hourdict[hour] = hourdict.get(hour, 0) + 1

for hr, occurance in sorted(hourdict.items()):       
	print(hr, occurance)
