# import media
#
# toy_story = media.Movie("Toy Story",
#                         "A story of a boy and his toys that come to life",
#                         "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
#                         "https://www.youtube.com/watch?v=vwyZH85NQC4")
# print(toy_story.storyline)
# toy_story.show_trailer()
# avatar = media.Movie("Avatar",
#                      "A marine on an alien planet",
#                      "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
#                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# print (avatar.storyline)
# avatar.show_trailer()
#
# print(media.Movie.__doc__)
# print(media.Movie.__name__)
# print(media.Movie.__module__)
# print(media.Movie.__bases__)
# print(media.Movie.__dict__)






# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

import socket, sys, getpass

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile = "abcd.txt"
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

me = "ankur.awl@gmail.com" # me == the sender's email address
you = "ankur.awl@gmail.com" # you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the envelope header.
# s = smtplib.SMTP('localhost')
# s.sendmail(me, [you], msg.as_string())
# s.quit()

try:
    smtpserver = smtplib.SMTP('smtp.live.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    print "connection to outlook successful"
    try:
        outlook_user = 'ankur.agwl@live.com' # str(raw_input('Enter email address: ')).lower().strip()
        outlook_pwd = 'Ghadi^66' # getpass.getpass('Enter password: ').strip()
        smtpserver.login(outlook_user, outlook_pwd)
        print("Authentication successful")
    except (smtplib.SMTPException), e:
        print("Authentication failed")
        print e
        smtpserver.close()
        sys.exit(1)
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
    print "connection to outlook failed"+'\n'
    print e
    sys.exit(1)

try:
    smtpserver.sendmail(me,you,msg.as_string())
except smtplib.SMTPException:
    print("Email could not be sent")
    print e
    smtpserver.close()
    sys.exit(1)

print("Email sent successfully")
smtpserver.close()
sys.exit(1)
