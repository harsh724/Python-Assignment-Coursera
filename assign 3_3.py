

rawscore = input("Enter Score: ")
outofrange = False
grade = None

try:
	score = float(rawscore)
except:
    print "Invalid connection, try again."
    exit()

if(score < 0.0):
    outofrange = True
elif (score > 1.0):
    outofrange = True
    
if(outofrange is True):    
    print "Entered number should be between 0.0 and 1.0."
    quit()
else:
    if(score >= 0.9):
        grade = "A" 
    elif(score >= 0.8):
        grade = "B"
    elif(score >= 0.7):
        grade = "C"
    elif(score >= 0.6):
        grade = "D"
    elif(score < 0.6):
        grade = "F"
    print (grade)
