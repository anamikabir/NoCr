import datetime
from htmlScraper import Get_All_Listings

OurList = {}

def get_new_posts(theUrl):
    res =  Get_All_Listings(theUrl)
    DateToday = datetime.datetime.now()
    currDate = DateToday.day
    for posts in res:
        if posts['postid'] in OurList:
            OurList[posts['postid']]= currDate
            print "Nothing happened"
        else:
            OurList[posts['postid']]= currDate
            print "This happened"
            # send email operation
    print str(OurList)
    # Get current date so application can delete enteries belong to previous day
    currMonth = DateToday.month 
    print str(currDate)+ " " + str(currMonth)
    



def del_old_entries():
    D = {}
    DateToday = datetime.datetime.now()
    currDate = DateToday.day
    
    for k,v in OurList.iteritems():
        if v == currDate:
           D[k]=v
    return D

"""
zc = raw_input("Enter Zipcode of the location: ")
print zc
"""

theUrl = "https://sfbay.craigslist.org/search/sfc/roo?hasPic=1&postedToday=1&bundleDuplicates=1&search_distance=2&postal=94103&min_price=800&max_price=1800&availabilityMode=0&private_room=1"

get_new_posts(theUrl)
#OurList = del_old_entries()
#print str(OurList)
print len(OurList)

