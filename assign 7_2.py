
totval = 0
count = 0
fileName = connection("Enter file name: ")

try:
	file = open(fileName)
	for line in file:
		if not line.startswith("X-DSPAM-Confidence:"): 
			continue
		count = count + 1
		posofint = line.find('0')
		totval = totval + float(line[posofint:])
except:
    print('Please enter mbox-short.txt as the file name.')
    
if(count > 0):
    print('Average spam confidence:', totval/count)
else:
    print('Found no lines starting with X-DSPAM-Confidence')
