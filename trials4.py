# import webbrowser
# import time

# def openbrowser():
#     print("Starting now... " + time.ctime())
#     time.sleep(5)
#     print("Opening web browser now... " + time.ctime())
#     webbrowser.open("www.amazon.com")
#
# open_browser()



# import os
# import string

# def rename_files():
#     # get file names...
#     filenames = os.listdir("C:\\Users\\aankur\\Dropbox\\___ ebooks")
#     print filenames
#
#     # rename each file... convert _ to space
#     path = "C:\\Users\\aankur\\Dropbox\\___ ebooks\\"
#     for x in filenames:
#         y = string.replace(x,'_',' ')
#         print("Renaming " + x + " to " + y)
#         os.rename(path+x, path+y)
#
# rename_files()



# import turtle

# def draw_circle_using_squares():
#     window = turtle.Screen()
#     window.bgcolor("yellow")
#
#     myt1 = turtle.Turtle()
#     myt1.shape("turtle")
#     myt1.color("red")
#     myt1.speed(0)
#     x = 0
#     while x < 360:
#         myt1.right(5)
#         draw_square(myt1)
#         x = x+5
#
#     window.exitonclick()
#
# def draw_square(myt):
#     for x in range(1,5):
#         myt.forward(100)
#         myt.right(90)
#
# def draw_circle(myt):
#     myt.circle(100)
#
# def draw_triangle(myt):
#     for x in range(1,4):
#         myt.forward(100)
#         myt.left(120)
#
# def draw_diamond(myt):
#     myt.forward(100)
#     myt.right(60)
#     myt.forward(100)
#     myt.right(120)
#     myt.forward(100)
#     myt.right(60)
#     myt.forward(100)
#     myt.right(120)
#
# def draw_flower():
#     window = turtle.Screen()
#     window.bgcolor("white")
#
#     myt1 = turtle.Turtle()
#     myt1.shape("classic")
#     myt1.color("blue")
#     myt1.speed(100)
#     x = 0
#     while x < 360:
#         myt1.right(5)
#         draw_diamond(myt1)
#         x = x+5
#
#     window.exitonclick()
#
# draw_circle_using_squares()
# draw_flower()




# from twilio.rest import TwilioRestClient
#
# # Your Account Sid and Auth Token from twilio.com/user/account
# account_sid = "AC111d1934bef1e2dc6cefa55af3a1d229"
# auth_token  = "d1bb56fef4107f51b045ce53f9843105"
# client = TwilioRestClient(account_sid, auth_token)
#
# message = client.messages.create(body="HELLO! How are things?",
#                                  to="+12066178384",    # Replace with your phone number
#                                  from_="+16467981444") # Replace with your Twilio number
# print message.sid


import urllib
import json

def read_text():
    quotes = open("C:\\Users\\aankur\\Downloads\\"+"movie_quotes.txt")
    contents = quotes.read()
    # print(contents)
    quotes.close()
    return contents

def check_profanity(text2check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text2check)
    output = connection.read()
    # print output
    connection.close()
    return output

isProfanityTxt = check_profanity(read_text())
print isProfanityTxt
isProfanityDict = json.loads(isProfanityTxt)
print isProfanityDict
if isProfanityDict['response'] == 'true':   # we have to use =='true' else this stmt will be always true because 'false' is a TRUE string not a boolean
    print "Profanity Alert!!!"
else:
    print "All fine"

