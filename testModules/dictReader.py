import pickle

D1 = {'6471175675': 24, '6471417279': 24, '6470744772': 24, '6470641752': 24, '6470559457': 24, '6471560462': 24, '6470812130': 24, '6471380459': 24, '6470526566': 24, '6471295485': 24, '6470460188': 24, '6470814559': 24, '6471271315': 24, '6471593395': 24, '6470575987': 24, '6471102175': 24, '6470534460': 24, '6471254347': 24, '6470781057': 24, '6470708131': 24, '6471446021': 24, '6470833166': 24, '6471045330': 24, '6470600123': 24, '6470730763': 24, '6470415614': 24, '6471354349': 24, '6471133608': 24, '6471429271': 24, '6470644877': 24, '6470646467': 24, '6470490795': 24}

def writefile():
    try:
        with open("PostList.txt","wb") as myDictFile:
            pickle.dump(D1,myDictFile)
    except:
        print "Write error"

def readfile():
    try:
        with open("PostList.txt","rb") as myDictFile:
            D1 = pickle.load(myDictFile)
            print type(D1)
            print D1
    except:
        print "Read error"

print len(D1)
writefile()
readfile()
