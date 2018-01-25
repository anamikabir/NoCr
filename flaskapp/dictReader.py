import pickle

def writefile(fileName,Dict):
    try:
        with open(fileName,"wb") as myDictFile:
            pickle.dump(Dict,myDictFile)
    except:
        print "Write error"

def readfile(fileName):
    D ={}
    try:
        with open(fileName,"rb") as myDictFile:
            D = pickle.load(myDictFile)
    except:
        print "Read error"
    return D

"""
# Test Code
D= {'1':1,'2':2}
MyFile = "PostList.txt"
writefile(MyFile,D)
D['3']=3
writefile(MyFile,D)
D = readfile(MyFile)
print type(D)
print str(D)
D = readfile("sdgsh.txt")
print str(D)
"""
