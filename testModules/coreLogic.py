import datetime
from htmlScraper import Get_All_Listings

OurList = {}

def get_new_posts(theUrl):
    res =  Get_All_Listings(theUrl)
    for posts in res:
        print str(posts)+"\n"
    # Get current date so application can delete enteries belong to previous day
    DateToday = datetime.datetime.now()
    currDate = DateToday.day
    #currMonth = DateToday.month 
    #print str(currDate)+ " " + str(currMonth)
    

theUrl = "https://sfbay.craigslist.org/search/sfc/roo?hasPic=1&postedToday=1&bundleDuplicates=1&search_distance=2&postal=94103&min_price=800&max_price=1800&availabilityMode=0&private_room=1"

get_new_posts(theUrl)
