# For sending email
import smtplib

# Import the email modules
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class email_helper:
    #List containing names and emails of all the intended receivers
    List_of_receivers={}
    #List containing username and password for TLS authorization with SMTP server
    USERNAME = " "
    PASSWORD = " "
    def __init__(self):
        try:
            with open("credentials.txt","r") as fp:
                parts = fp.read().rstrip().split(" ")
                #print parts
                self.USERNAME = parts[0]
                self.PASSWORD = parts[1]
                #print self.USERNAME + "\t" + self.PASSWORD
                fp.close()
            with open("contacts.txt","r") as cp:
                line = cp.readline()
                while line:
                    parts = line.rstrip().split("|")
                    #print parts
                    self.List_of_receivers[parts[1]]=parts[0]
                    line=cp.readline()
                cp.close()
        except:
            print "Error reading files"
    """
        finally:
            fp.close()
            cp.close()
    """
    
    # Method to send email using SMTP library (using gmail smpt server with TLS port and authentication -- can use different SMTP server too)
    def create_mail_alert(self,Subject, MsgString):
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(self.USERNAME,self.PASSWORD)

        #For sending emails to all the persons in the contact list
        for k,v in self.List_of_receivers.iteritems():
            msg = MIMEMultipart('alternative')
            msg['Subject'] = Subject
            msg['From'] = self.USERNAME
            msg['To'] = k
        
            text = MsgString.format(v)

            msg.attach(MIMEText(text, 'plain'))
            s.sendmail(self.USERNAME, k, msg.as_string())

        s.quit()


"""
myEmailHelper = email_helper()
myEmailHelper.create_mail_alert("Alert","Hi {}!\nThis is a test email.\nHere is the link you wanted:\nhttps://www.python.org")
"""
