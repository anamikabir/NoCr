import time
import atexit
import datetime

from flask import Flask

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

#To import read and write dictionary functionality using pickle
from dictReader import *

#To import html parsing code to retrieve listings
from htmlScraper import Get_All_Listings

#To import functionality to create and send an email notification
from emailHelper import email_helper

import logging
logging.basicConfig()

ListingFile = "PostList.txt"

currentListings = readfile(ListingFile)
Lockcurr = False
theUrl = "https://sfbay.craigslist.org/search/sfc/roo?hasPic=1&postedToday=1&bundleDuplicates=1&search_distance=2&postal=94103&min_price=800&max_price=1800&availabilityMode=0&private_room=1"

# Function to send notifications for every new post
def send_notifications():
    global theUrl,ListingFile,Lockcurr,currentListings
    res =  Get_All_Listings(theUrl)
    DateToday = datetime.datetime.now()
    currDate = DateToday.day
    #print len(res)
    for posts in res:
        if posts['postid'] in currentListings:
            currentListings[posts['postid']]= currDate
            #print "Nothing happened"
        else:
            currentListings[posts['postid']]= currDate
            #print "Email notification"
            myEmailHelper = email_helper()
            BodyContents = "Hi {}!\n\nThis is a notification email.\n\n"
            EmailSubject = posts['title']
            BodyContents += posts['title']+"\n"
            if 'price' in posts:
                BodyContents += "Rent (Price in USD): "+posts['price']+"\n"
            if 'hood' in posts:
                BodyContents += "Neighbourhood: "+posts['hood']+"\n"
            BodyContents += "\nLink to Follow: " +posts['url']+"\n\nRegards,\nNoCr Notification Team\n"
            #print "Sending the email"+ EmailSubject
            myEmailHelper.create_mail_alert(EmailSubject,BodyContents)
    #print "Done with all records"
    while True:
        if not Lockcurr:
            Lockcurr = True
            #print "Entering lock -- write into file"
            writefile(ListingFile,currentListings)
            Lockcurr = False
            #print "Exiting lock -- write into file"
            break

def del_old_contents():
    global theUrl,ListingFile,Lockcurr,currentListings
    D = {}
    DateToday = datetime.datetime.now()
    currDate = DateToday.day
    
    for k,v in currentListings.iteritems():
        if v == currDate:
           D[k]=v
    #print len(currentListings)
    #print len(D)
    currentListings = D
    while True:
        if not Lockcurr:
            Lockcurr = True
            #print "Entering lock -- after deletion"
            writefile(ListingFile,currentListings)
            Lockcurr = False
            #print "Exiting lock -- after deletion"
            break

app = Flask(__name__)

scheduler = BackgroundScheduler()
#scheduler.start()
scheduler.add_job(
    func=send_notifications,
    trigger=IntervalTrigger(minutes=5),
    id='notification_job',
    name='Send notification for new posts every 5 mins',
    replace_existing=True)

scheduler.add_job(
    func=del_old_contents,
    trigger=IntervalTrigger(minutes=30),
    id='del_old_dict_job',
    name='Delete older post enteries - runs once every 30 mins',
    replace_existing=True)

scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    app.run()
