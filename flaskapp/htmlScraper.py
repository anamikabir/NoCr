from lxml import html
import requests



def Get_All_Listings(theUrl):
    # use request libraray to get the page contents and lxml parser to get a tree of the html contents
    try:
        page = requests.get(theUrl)
    except:
        print "Exception handled"
        return []
    tree = html.fromstring(page.content)
    #print page.content

    #List to store all post info
    FinalList = []

    #Retrive unique listings and total number of unique listings
    Results = tree.xpath('//li[@class="result-row"]')
    #print len(Results)

    #for each unique listing retrieve URL , postid , title, price and neighbourhood information
    for res in Results:
        # Create a Dictionary of post contents
        D={}
        # To retrieve link to post , unique post id and title of the post
        LinkURL = res.xpath('./p[@class="result-info"]/a[@class="result-title hdrlnk"]')
        if len(LinkURL) == 1:
            D['postid']=LinkURL[0].attrib['data-id']
            D['title']=LinkURL[0].text
            D['url']=" "+LinkURL[0].attrib['href']+" "
        # To retrieve price info from result -> Won't be included if missing
        Price = res.xpath('./p[@class="result-info"]/span[@class="result-meta"]/span[@class="result-price"]/text()')
        if len(Price) == 1:
            D['price']= Price[0]
        # To retrieve Neighbourhood info -> Won't be included if missing
        Neighbourhood = res.xpath('./p[@class="result-info"]/span[@class="result-meta"]/span[@class="result-hood"]/text()')
        if len(Neighbourhood) == 1:
            D['hood']= Neighbourhood[0][2:-1]
        #Append if not an empty post (Not really possible -- just a precautionary measure)
        if len(D) > 0 :
            FinalList.append(D)

    #Get list of duplicate listings (just to verify that number of unique results + number of duplicates = total number of listings
    Duplicate = tree.xpath('//li[@class="result-row duplicate-row"]')
    #print len(Duplicate)

    #Get total number of listings of URL
    Listings = tree.xpath('//a[@class="result-title hdrlnk"]')
    #print len(Listings)

    return FinalList    

"""
#URL to be scraped 
theUrl = "https://sfbay.craigslist.org/search/sfc/roo?hasPic=1&postedToday=1&bundleDuplicates=1&search_distance=2&postal=94103&min_price=800&max_price=1800&availabilityMode=0&private_room=1"

ResList = Get_All_Listings(theUrl)

# For printing the retrieved post information
for posts in ResList:
    print str(posts) + "\n"
"""
