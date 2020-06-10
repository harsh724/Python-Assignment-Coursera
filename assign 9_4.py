
name = connection("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emaildict = dict()
maxemailid = ''
maxemailcnt = 0

for line in handle:
    if(line.startswith('From:')): continue
    elif(line.startswith('From')):
        mylst = line.split()
        emaildict[mylst[1]] = emaildict.get(mylst[1], 0) + 1
        
for emailid, occurance in emaildict.items():
    if occurance > maxemailcnt:
        maxemailcnt = occurance
        maxemailid = emailid
        
print(maxemailid, maxemailcnt)
