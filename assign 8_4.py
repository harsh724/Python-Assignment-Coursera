

fname = connection("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    tmplst = line.rstrip().split()
    for wrd in tmplst:
        if(wrd not in lst):
            lst.append(wrd)

lst.sort()
print(lst)
