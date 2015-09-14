#!/Users/aankur/Dropbox/code/python/practice/trial.py

def hello(message,*remaining):
    # message = 'Hello World'
    print(message.upper(),message,message,sep=":",end="....")
    print()
    print(len(remaining))
    print()
    for i in range(len(remaining)):
        print(remaining[i])
        print()
    print() 
    return message

# hello("Not Hello World", "Hey, How are you?", "Hi", "How are you doing","are you sure?")


def passingArgs(message,max_len,**arglist):
    #trying to test how to pass arguments in diff ways... dictionary?
    print(message)
    #print()
    print(arglist)
    #print()
    return dict([(key, arglist[key]) for i, key in enumerate(arglist.keys()) if i < max_len])


# print(passingArgs("Hello", 4 ,key1=10, key2=9, key3=8, key4=7, key5=6, key6=5))


def checkClosureOuter(outerArg):
    def checkClosureMiddle(middleArg): 
        def checkClosureInner(innerArg):
            print("Inner Arg = ",innerArg)
            print("Middle Arg = ",middleArg)
            print("Middle Arg2 = ",middleArg2)
            print("Outer Arg = ",outerArg)
            return (innerArg * outerArg * middleArg * middleArg2)
        middleArg = middleArg * -1 
        middleArg2 = -1 
        return checkClosureInner 
    return checkClosureMiddle


##f1 = checkClosureOuter(10)
##f2 = f1(9) 
##print("**********",f2(9)) 
##print("**********",f2(8)) 
##print("**********",f2(7)) 
##print("**********",f2(6)) 
##print("**********",f2(5)) 
##print("**********",f2(4)) 


##try:
##    print(1/0) 
##except ZeroDivisionError:
##    print("Division by zero is not allowed.") 



##try:
##    the_file = open("the_parrot")
##except Exception as args:
##    print(args)
##    print(type(args))
##    if isinstance(args,FileNotFoundError):
##        print("Sorry, 'the_parrot' has apparently joined the choir invisible.")
##    else:
##        print("Congratulation! you have managed to trip error:",type(args))



##def tryingException():
##    while True:
##        try:
##            x = int(input("Please enter a number: "))
##            print("After the input")
##            break
##        except IOError:
##            print("Oops! There was some IO error.  Try again...")
##        except ValueError: 
##            print("Oops! That was no valid number.  Try again...")
##
##
##try:
##    tryingException()
##except:
##    print("Outer Exception")




##x = input("Enter a number to be evaluated: ")
##if isinstance(x,int):
##    print(x,"is integer")
##elif isinstance(x,str):
##    print(x,"is string")
##else: 
##    print(x,"is not integer")
###print("type of '"+x+"' is",type(x))



##f = open('trial.py','r')
##f2= open('outputfile.txt','w') 
##for line in f:
##    #print(line,end='') 
##    print(line,end='',file=f2) 
##f.close() 
##f2.close() 
##
##f3 = open('outputfile.txt','r')
##c = f3.read(1)
##while len(c)>0:
##    if isalpha(c): print(c,end='')
##    c = f3.read(1) 
##print() 




##import sys
##print("Arguments passed:",sys.argv)
##try:
##    for line in open(sys.argv[1],'r'):
##        print(line,end='')
##except:
##    for line in sys.stdin:
##        print(line) 




##from Object1 import * 
##obj1 = Object1() 
##print(obj1)
##obj11 = Object1_1()
##print(obj11) 




##class TRY:
##    def setx(self,x):
##        self.x = x
##    def printx(self):
##        print("Value of x is",self.x)
##
##class TRY2:
##    def sety(self,y):
##        self.y = y
##        self.x = y
##    def printy(self):
##        print("Value of y is",self.y) 
##
##
##f = TRY()
##f.setx(5)
##f.printx()
##
##f2 = TRY2()
##f2.sety(10)
##f2.printy()
##print()
##print()
##
##TRY2.z = 15
##print(f2.z)
##f2.z = 20
##print(f2.z)
##print()
##print()
##
##del f2.y
##try:
##    f2.printy()
##except:
##    print("Unable to print the value of : f2 > y")
##
##try:
##    TRY.printx(f2)  #f2 is not an object of TRY, but still we can call TRY method for f2
##except:
##    print("Unable to print the value of : f2 > x")
##
##try:
##    TRY2.printy(f2)
##except:
##    print("Unable to print the value of : f2 > y")
##
##print("Variables of TRY are:")
##print(vars(TRY))
##print("Variables of TRY2 are:")
##print(vars(TRY2))
##print("Variables of f are:")
##print(vars(f))
##print("Variables of f2 are:")
##print(vars(f2))



import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))
        time.sleep(4)
        print("{} finished!".format(self.getName()))
    
if __name__ == '__main__':
    for x in range(10):
        mythread = MyThread(name = "Thread-{}".format(x+1))
        mythread.start()
        time.sleep(1) 




        
        
        
## ------------------------------------------------------------------ 
## Python 2.7 practice - Udacity Course 
## ------------------------------------------------------------------ 
# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.44159

#ENTER CODE BELOW HERE

print str(x+0.5)[:str(x+0.5).find('.')] 



###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads 
# the same backwards as forwards. Make a program 
# that checks if a word is a palindrome. 
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise. 
# The word contains lowercase letters a-z and 
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

word = "madam"
# test case 2
word = "madman" # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###

is_palindrome = word.find( word[::-1])

# TESTING
print is_palindrome
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"
#####################################################################################
#####################################################################################








#####################################################################################
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    totalDays = daysInYear(year1) - daysFromStartOfYearTill(year1,month1,day1) 
    #print "-- ", year1 , " has " , totalDays, " days from -1-1 to -",month1,"-",day1 
    i = year1 + 1 
    while i < year2: 
        totalDays = totalDays + daysInYear(i) 
        i=i+1 
    #print "For " , (year1) , " to " , (year2-1) , " we got " , totalDays 
    totalDays = totalDays + daysFromStartOfYearTill(year2,month2,day2) 
    #print "For " , (year1) , " to " , (year2) , " we got " , totalDays 
    if year1 == year2:
        totalDays = totalDays - daysInYear(year2) 
    #print year1,"-",month1,"-",day1," to ",year2,"-",month2,"-",day2," there are ",totalDays," days as per our calculation" 
    return totalDays


# Routine to find whether an year is leap year or not  
def daysInYear(year):
    if ( (year %4==0 and year %100<>0) or (year %400==0) ): 
        return 366 
    return 365 


# Routine to find count of days from start of this year till date 
def daysFromStartOfYearTill(year,month,day):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    daysFromStart = 0 
    i=0
    while i < month-1:
        daysFromStart = daysFromStart + daysOfMonths[i]
        i=i+1 
    daysFromStart = daysFromStart + day 
    if month > 2:
        daysFromStart = daysFromStart + daysInYear(year)-365 
    #print "From ",year,"-1-1 till " , year , "-" , month , "-" , day, ", there are ", daysFromStart, " days."
    return daysFromStart


# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,1,1,2011,1,1), 0),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        #print "--- Test: These dates ",args," should give answer as ",answer," days in between" 
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"
        #print "" 

test()
#####################################################################################
#####################################################################################















#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
    strValue = str(value).zfill(10)
    for i in xrange(len(strValue)): 
        num = int(strValue[i])
        print "|"+'00000*****'[0:10-num]+"   "+'00000*****'[10-num:]+"|"

        
        
###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|

#########################################################################
#########################################################################







############################################################################
############################################################################
# 2 Gold Stars
# One way search engines rank pages
# is to count the number of times a
# searcher clicks on a returned link.
# This indicates that the person doing
# the query thought this was a useful
# link for the query, so it should be
# higher in the rankings next time.
# (In Unit 6, we will look at a different
# way of ranking pages that does not depend
# on user clicks.)
# Modify the index such that for each url in a
# list for a keyword, there is also a number
# that counts the number of times a user
# clicks on that link for this keyword.
# The result of lookup(index,keyword) should
# now be a list of url entries, where each url
# entry is a list of a url and a number
# indicating the number of times that url
# was clicked for this query keyword.
# You should define a new procedure to simulate
# user clicks for a given link:
# record_user_click(index,word,url)
# that modifies the entry in the index for
# the input word by increasing the count associated
# with the url by 1.
# You also will have to modify add_to_index
# in order to correctly create the new data
# structure, and to prevent the repetition of
# entries as in homework 4-5.

def record_user_click(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            for urlclickpair in entry[1]: 
                if urlclickpair[0] == url: 
                    urlclickpair[1] += 1 
    return 

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            for urlclickpair in entry[1]: 
                if urlclickpair[0]==url: 
                    return 
            entry[1].append([url,0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url,0]]])

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return '''<html> <body> This is a test page for learning to crawl!
<p> It is a good idea to
<a href="http://www.udacity.com/cs101x/crawling.html">
learn to crawl</a> before you try to
<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body></html>'''

        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.
</body> </html>'''

        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '''<html> <body> I cant get enough
<a href="http://www.udacity.com/cs101x/index.html">crawling</a>!</body></html>'''

        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html><body>The magic words are Squeamish Ossifrage!</body></html>'
    except:
        return ""
    return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

#Here is an example showing a sequence of interactions:
index = crawl_web('http://www.udacity.com/cs101x/index.html')
print lookup(index, 'good')
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 0]]
record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
print lookup(index, 'good')
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 1]]

############################################################################
############################################################################
############################################################################







############################################################################
############################################################################
############################################################################
# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.
#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    # YOUR CODE
    list = [] 
    list2 = [] 
    prev = 0 
    n = len(string) 
    for i in xrange(n): 
        x = int(string[i]) 
        if i==0:
            prev = x 
            list.append(x) 
        else: 
            if x <= prev: 
                list2.append(x) 
            else: 
                if list2 <> []:
                    list.append(list2) 
                    list2 = [] 
                list.append(x) 
                prev = x 
    if list2 <> []:
        list.append(list2) 
    return list 

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result

############################################################################
############################################################################
############################################################################





############################################################################
############################################################################
############################################################################
# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible 
# algorithm or even language of the clear text message, one could perform 
# frequency analysis. This process could be described as simply counting 
# the number of times a certain symbol occurs in the given text. 
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
#
# The input to the function will be an encrypted body of text that only contains 
# the lowercase letters a-z. 
# As output you should return a list of the normalized frequency 
# for each of the letters a-z. 
# The normalized frequency is simply the number of occurrences, i, 
# divided by the total number of characters in the message, n.

def freq_analysis(message):
    freq_list=[]
    listofletters = "abcdefghijklmnopqrstuvwxyz"
    n = len(message) 
    for x in listofletters: 
        freq_list.append(message.count(x)/(n*1.0)) 
    return freq_list

#Tests
print 
print freq_analysis("abcd")
#>>> [0.25, 0.25, 0.25, 0.25, 0.0, ..., 0.0]
print 

print freq_analysis("adca")
#>>> [0.5, 0.0, 0.25, 0.25, 0.0, ..., 0.0]
print 

print freq_analysis('bewarethebunnies')
#>>> [0.0625, 0.125, 0.0, 0.0, ..., 0.0]

############################################################################
############################################################################
############################################################################








############################################################################
############################################################################
############################################################################
# 1 Gold Star
# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.
# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.

def split_string(source,splitlist):
    res = [source]
    for sep in splitlist:
        source, res = res, []
        for seq in source:
            res += seq.split(sep)
    return [resvalues for resvalues in res if resvalues != '']  

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

############################################################################
############################################################################
############################################################################





















############################################################################
############################################################################
############################################################################
#Feeling Lucky
#In Unit 6, we implemented a page ranking algorithm, but didn't finish the final
#step of using it to improve our search results. For this question, you will use
#the page rankings to produce the best output for a given query.
#Define a procedure, lucky_search, that takes as input an index, a ranks
#dictionary (the result of compute_ranks), and a keyword, and returns the one
#URL most likely to be the best site for that keyword. If the keyword does not
#appear in the index, lucky_search should return None.

def lucky_search(index, ranks, keyword):
    resulturls = lookup(index,keyword) 
    if resulturls is None:
        return None
    else:
        besturlrank=0 
        besturl='' 
        for x in resulturls:
            if ranks[x] > besturlrank:
                besturlrank = ranks[x] 
                besturl = x 
        return besturl 

cache = {
   'http://udacity.com/cs101x/urank/index.html': """<html>
<body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">World's Best Hummus</a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">Kathleen's Hummus Recipe</a>
</ul>

For more expert opinions, check out the 
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a> 
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>

""",
   'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from 
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try 
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>

<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>

<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>.
<li> Force her to make hummus for you.
</ol>

</body>
</html>

""",
   'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>
<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>
</body>
</html>
""",
}

def get_page(url):
    if url in cache:
        return cache[url]
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
    
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


#Here's an example of how your procedure should work on the test site: 

index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)

print lucky_search(index, ranks, 'Hummus')
#>>> http://udacity.com/cs101x/urank/kathleen.html

print lucky_search(index, ranks, 'the')
#>>> http://udacity.com/cs101x/urank/nickel.html

print lucky_search(index, ranks, 'babaganoush')
#>>> None

############################################################################
############################################################################
############################################################################













############################################################################
############################################################################
############################################################################
# One Gold Star
# Question 1-star: Stirling and Bell Numbers
# The number of ways of splitting n items in k non-empty sets is called
# the Stirling number, S(n,k), of the second kind. For example, the group 
# of people Dave, Sarah, Peter and Andy could be split into two groups in 
# the following ways.
# 1.   Dave, Sarah, Peter         Andy
# 2.   Dave, Sarah, Andy          Peter
# 3.   Dave, Andy, Peter          Sarah
# 4.   Sarah, Andy, Peter         Dave
# 5.   Dave, Sarah                Andy, Peter
# 6.   Dave, Andy                 Sarah, Peter
# 7.   Dave, Peter                Andy, Sarah
# so S(4,2) = 7
# If instead we split the group into one group, we have just one way to 
# do it.
# 1. Dave, Sarah, Peter, Andy
# so S(4,1) = 1
# or into four groups, there is just one way to do it as well
# 1. Dave        Sarah          Peter         Andy
# so S(4,4) = 1
# If we try to split into more groups than we have people, there are no
# ways to do it.
# The formula for calculating the Stirling numbers is
#  S(n, k) = k*S(n-1, k) + S(n-1, k-1)
# Furthermore, the Bell number B(n) is the number of ways of splitting n 
# into any number of parts, that is,
# B(n) is the sum of S(n,k) for k =1,2, ... , n.
# Write two procedures, stirling and bell. The first procedure, stirling 
# takes as its inputs two positive integers of which the first is the 
# number of items and the second is the number of sets into which those 
# items will be split. The second procedure, bell, takes as input a 
# positive integer n and returns the Bell number B(n).

def stirling(n,k):
    if k==0 or n<k:
        return 0
    if k==1 or n==k: 
        return 1 
    return (k*stirling(n-1,k) ) + stirling(n-1,k-1) 

def bell(n):
    sum = 0 
    for k in range(1,n+1): 
        sum += stirling(n,k) 
    return sum 

print '-----------'
print stirling(1,1)
#>>> 1
print '-----------'
print stirling(2,1)
#>>> 1
print stirling(2,2)
#>>> 1
print stirling(2,3)
#>>>0
print '-----------'
print stirling(3,1)
#>>> 1
print stirling(3,2)
#>>> 3
print stirling(3,3)
#>>> 1
print '-----------'
print stirling(4,1)
#>>> 1
print stirling(4,2)
#>>> 7
print stirling(4,3)
#>>> 6
print stirling(4,4)
#>>> 1
print '-----------'
print stirling(5,1)
#>>> 1
print stirling(5,2)
#>>> 15
print stirling(5,3)
#>>> 25
print stirling(5,4)
#>>> 10
print stirling(5,5)
#>>> 1
print '-----------'
print stirling(20,15)
#>>> 452329200
print '-----------'
print '-----------'
print '-----------'
print bell(1)
#>>> 1
print bell(2)
#>>> 2
print bell(3)
#>>> 5
print bell(4)
#>>> 15
print bell(5)
#>>> 52
print bell(15)
#>>> 1382958545
print '-----------'
############################################################################
############################################################################
############################################################################

















############################################################################
############################################################################
############################################################################
# Two Gold Stars
# Question 2: Combatting Link Spam
# One of the problems with our page ranking system is pages can
# collude with each other to improve their page ranks.  We consider
# A->B a reciprocal link if there is a link path from B to A of length
# equal to or below the collusion level, k.  The length of a link path
# is the number of links which are taken to travel from one page to the
# other.
# If k = 0, then a link from A to A is a reciprocal link for node A,
# since no links needs to be taken to get from A to A.
# If k=1, B->A would count as a reciprocal link  if there is a link
# A->B, which includes one link and so is of length 1. (it requires
# two parties, A and B, to collude to increase each others page rank).
# If k=2, B->A would count as a reciprocal link for node A if there is
# a path A->C->B, for some page C, (link path of length 2),
# or a direct link A-> B (link path of length 1).
# Modify the compute_ranks code to
#   - take an extra input k, which is a non-negative integer, and
#   - exclude reciprocal links of length up to and including k from
#     helping the page rank.

def compute_ranks(graph,k):
    # k -> collusion level
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                pathlength = getlinkpathlengthfromAtoB(graph,page,node,k)
                if (pathlength is None) or (pathlength > k):
                    if (page in graph[node]):
                        newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks

def getlinkpathlengthfromAtoB(graph,linkA,linkB,k):
    # k -> Collusion level
    if linkA == linkB:
        return 0
    if k==0:
        return None
    if linkA not in graph:
        return None
    if linkB in graph[linkA]:
        return 1
    minlinklength = None
    for eachlink in graph[linkA]:
        currentlinklength = getlinkpathlengthfromAtoB(graph,eachlink,linkB,k-1)
        if currentlinklength is not None:
            if (minlinklength is None):
                minlinklength = 1 + currentlinklength
            else:
                minlinklength = min(minlinklength, 1 + currentlinklength)
    return minlinklength

# For example
g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

print getlinkpathlengthfromAtoB(g,'a','b',10)
print getlinkpathlengthfromAtoB(g,'a','c',10)
print getlinkpathlengthfromAtoB(g,'a','d',10)
print getlinkpathlengthfromAtoB(g,'a','a',10)
print getlinkpathlengthfromAtoB(g,'b','b',10)
print getlinkpathlengthfromAtoB(g,'b','c',10)
print getlinkpathlengthfromAtoB(g,'b','d',10)
print getlinkpathlengthfromAtoB(g,'c','c',10)
print getlinkpathlengthfromAtoB(g,'c','d',10)
print getlinkpathlengthfromAtoB(g,'d','d',10)
print getlinkpathlengthfromAtoB(g,'b','a',10)
print getlinkpathlengthfromAtoB(g,'c','a',10)
print getlinkpathlengthfromAtoB(g,'d','a',10)
print getlinkpathlengthfromAtoB(g,'c','b',10)
print getlinkpathlengthfromAtoB(g,'d','b',10)
print getlinkpathlengthfromAtoB(g,'d','c',10)
print
print

print compute_ranks(g, 0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

print compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

print compute_ranks(g, 2)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}
############################################################################
############################################################################
############################################################################































# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# THREE GOLD STARS
# Question 3-star: Elementary Cellular Automaton
# Please see the video for additional explanation.
# A one-dimensional cellular automata takes in a string, which in our
# case, consists of the characters '.' and 'x', and changes it according
# to some predetermined rules. The rules consider three characters, which
# are a character at position k and its two neighbours, and determine
# what the character at the corresponding position k will be in the new
# string.
# For example, if the character at position k in the string  is '.' and
# its neighbours are '.' and 'x', then the pattern is '..x'. We look up
# '..x' in the table below. In the table, '..x' corresponds to 'x' which
# means that in the new string, 'x' will be at position k.
# Rules:
#          pattern in         position k in        contribution to
# Value    current string     new string           pattern number
#                                                  is 0 if replaced by '.'
#                                                  and value if replaced
#                                                  by 'x'
#   1       '...'               '.'                        1 * 0
#   2       '..x'               'x'                        2 * 1
#   4       '.x.'               'x'                        4 * 1
#   8       '.xx'               'x'                        8 * 1
#  16       'x..'               '.'                       16 * 0
#  32       'x.x'               '.'                       32 * 0
#  64       'xx.'               '.'                       64 * 0
# 128       'xxx'               'x'                      128 * 1
#                                                      ----------
#                                                           142
# To calculate the patterns which will have the central character x, work
# out the values required to sum to the pattern number. For example,
# 32 = 32 so only pattern 32 which is x.x changes the central position to
# an x. All the others have a . in the next line.
# 23 = 16 + 4 + 2 + 1 which means that 'x..', '.x.', '..x' and '...' all
# lead to an 'x' in the next line and the rest have a '.'
# For pattern 142, and starting string
# ...........x...........
# the new strings created will be
# ..........xx...........  (generations = 1)
# .........xx............  (generations = 2)
# ........xx.............  (generations = 3)
# .......xx..............  (generations = 4)
# ......xx...............  (generations = 5)
# .....xx................  (generations = 6)
# ....xx.................  (generations = 7)
# ...xx..................  (generations = 8)
# ..xx...................  (generations = 9)
# .xx....................  (generations = 10)
# Note that the first position of the string is next to the last position
# in the string.
# Define a procedure, cellular_automaton, that takes three inputs:
#     a non-empty string,
#     a pattern number which is an integer between 0 and 255 that
# represents a set of rules, and
#     a positive integer, n, which is the number of generations.
# The procedure should return a string which is the result of
# applying the rules generated by the pattern to the string n times.

def cellular_automaton(originalString,patternNumber,generation):
    patternMap = generatePatternMap(patternNumber,8)
    #print patternMap
    for i in range(generation):
        originalString = getNextGeneration(originalString,patternMap)
    return originalString


def generatePatternMap(patternNumber,maxSize):
    #169 to {'000':'1','001':'0', ... }
    x = patternNumber
    patternMap = {}
    for i in range(maxSize-1,-1,-1):
        y = convertNumToBitString(i,3)
        if x >= 2**i:
            patternMap[y] = 'x'
            x = x - 2**i
        else:
            patternMap[y] = '.'
    return patternMap

def convertNumToBitString(num,size):
    bitString = ''
    for i in range(size-1,-1,-1):
        if num >= 2**i:
            bitString = bitString + 'x'
            num = num - 2**i
        else:
            bitString = bitString + '.'
    return bitString

def getNextGeneration(old,patternMap):
    old = old + old
    new = ''
    for i in range(8):
        new = new + patternMap[ old[i-1] + old[i] + old[i+1] ]
    return new

print cellular_automaton('.x.x.x.x.', 17, 2)
#>>> xxxxxxx..
print cellular_automaton('.x.x.x.x.', 249, 3)
#>>> .x..x.x.x
print cellular_automaton('...x....', 125, 1)
#>>> xx.xxxxx
print cellular_automaton('...x....', 125, 2)
#>>> .xxx....
print cellular_automaton('...x....', 125, 3)
#>>> .x.xxxxx
print cellular_automaton('...x....', 125, 4)
#>>> xxxx...x
print cellular_automaton('...x....', 125, 5)
#>>> ...xxx.x
print cellular_automaton('...x....', 125, 6)
#>>> xx.x.xxx
print cellular_automaton('...x....', 125, 7)
#>>> .xxxxx..
print cellular_automaton('...x....', 125, 8)
#>>> .x...xxx
print cellular_automaton('...x....', 125, 9)
#>>> xxxx.x.x
print cellular_automaton('...x....', 125, 10)
#>>> ...xxxxx
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------





























































## ---------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------
# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# -----------------------------------------------------------------------------

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know
# what they are doing, having taken our web development class). However, it is
# up to you to create a data structure that manages the game-network information
# and to define several procedures that operate on the network.
#
# In a website, the data is stored in a database. In our case, however, all the
# information comes in a big string of text. Each pair of sentences in the text
# is formatted as follows:
#
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
#
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
#
# Note that each sentence will be separated from the next by only a period. There will
# not be whitespace or new lines between sentences.
#
# Your friend records the information in that string based on user activity on
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below.
#
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged
# to define any additional helper procedures that can assist you in accomplishing
# a task. You are encouraged to test your code by using print statements and the
# Test Run button.
# -----------------------------------------------------------------------------

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# -----------------------------------------------------------------------------
# create_data_structure(string_input):
#   Parses a block of text (such as the one above) and stores relevant
#   information into a data structure. You are free to choose and design any
#   data structure you would like to use to manage the information.
#
# Arguments:
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not
#   list B's connections or liked games.
#
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
#
# Return:
#   The newly created network data structure
def create_data_structure(string_input):
    return network

# ----------------------------------------------------------------------------- #
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        #
# ----------------------------------------------------------------------------- #

# -----------------------------------------------------------------------------
# get_connections(network, user):
#   Returns a list of all the connections that user has
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    return []

# -----------------------------------------------------------------------------
# get_games_liked(network, user):
#   Returns a list of all the games a user likes
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    return []

# -----------------------------------------------------------------------------
# add_connection(network, user_A, user_B):
#   Adds a connection from user_A to user_B. Make sure to check that both users
#   exist in network.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return:
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    return network

# -----------------------------------------------------------------------------
# add_new_user(network, user, games):
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no
#   connections to begin with.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return:
#   The updated network with the new user and game preferences added. The new user
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    return network

# -----------------------------------------------------------------------------
# get_secondary_connections(network, user):
#   Finds all the secondary connections (i.e. connections of connections) of a
#   given user.
#
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return:
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
#
# NOTE:
#   It is OK if a user's list of secondary connections includes the user
#   himself/herself. It is also OK if the list contains a user's primary
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    return []

# -----------------------------------------------------------------------------
# connections_in_common(network, user_A, user_B):
#   Finds the number of people that user_A and user_B have in common.
#
# Arguments:
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return:
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def connections_in_common(network, user_A, user_B):
    return 0

# -----------------------------------------------------------------------------
# path_to_friend(network, user_A, user_B):
#   Finds a connections path from user_A to user_B. It has to be an existing
#   path but it DOES NOT have to be the shortest path.
#
# Arguments:
#   network: The network you created with create_data_structure.
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
#
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam,
#   who is connected with Zed.
#
# NOTE:
#   You must solve this problem using recursion!
#
# Hints:
# - Be careful how you handle connection loops, for example, A is connected to B.
#   B is connected to C. C is connected to B. Make sure your code terminates in
#   that case.
# - If you are comfortable with default parameters, you might consider using one
#   in this procedure to keep track of nodes already visited in your search. You
#   may safely add default parameters since all calls used in the grading script
#   will only include the arguments network, user_A, and user_B.
def path_to_friend(network, user_A, user_B):
    # your RECURSIVE solution here!
    return None

# Make-Your-Own-Procedure (MYOP)
# -----------------------------------------------------------------------------
# Your MYOP should either perform some manipulation of your network data
# structure (like add_new_user) or it should perform some valuable analysis of
# your network (like path_to_friend). Don't forget to comment your MYOP. You
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

#net = create_data_structure(example_input)
#print net
#print path_to_friend(net, "John", "Ollie")
#print get_connections(net, "Debra")
#print add_new_user(net, "Debra", [])
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "Freda")
#print get_secondary_connections(net, "Mercedes")
#print connections_in_common(net, "Mercedes", "John")

## ---------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------
















## ---------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------

from collections import namedtuple
import sqlite3

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file"),
    Link(15, 62443, 1333900877.0, 1244,
         "Why vector icons don't work",
         "http://www.pushing-pixels.org/2011/11/04/about-those-vector-icons.html"),
    Link(14, 30650, 1334013659.0, 3,
         "Python - Getting Data Into Graphite - Code Examples",
         "http://coreygoldberg.blogspot.com/2012/04/python-getting-data-into-graphite-code.html"),
    Link(16, 15330, 1333985877.0, 9,
         "Mozilla: The Web as the Platform and The Kilimanjaro Event",
         "https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.planning/Y9v46wFeejA"),
    Link(18, 62443, 1333939389.0, 104,
         "github is making me feel stupid(er)",
         "http://www.serpentine.com/blog/2012/04/08/github-is-making-me-feel-stupider/"),
    Link(19, 6937, 1333949857.0, 39,
         "BitC Retrospective: The Issues with Type Classes",
         "http://www.bitc-lang.org/pipermail/bitc-dev/2012-April/003315.html"),
    Link(20, 51067, 1333974585.0, 14,
         "Object Oriented C: Class-like Structures",
         "http://cecilsunkure.blogspot.com/2012/04/object-oriented-c-class-like-structures.html"),
    Link(10, 23944, 1333943632.0, 188,
         "The LOVE game framework version 0.8.0 has been released - with GLSL shader support!",
         "https://love2d.org/forums/viewtopic.php?f=3&amp;t=8750"),
    Link(22, 39191, 1334005674.0, 11,
         "An open letter to language designers: Please kill your sacred cows. (megarant)",
         "http://joshondesign.com/2012/03/09/open-letter-language-designers"),
    Link(21, 3777, 1333996565.0, 2,
         "Developers guide to Garage48 hackatron",
         "http://martingryner.com/developers-guide-to-garage48-hackatron/"),
    Link(24, 48626, 1333934004.0, 17,
         "An R programmer looks at Julia",
         "http://www.r-bloggers.com/an-r-programmer-looks-at-julia/")]

# links is a list of Link objects. Links have a handful of properties. For
# example, a Link's number of votes can be accessed by link.votes if "link" is a
# Link.

# make and populate a table
db = sqlite3.connect(':memory:')
db.execute('create table links ' +
           '(id integer, submitter_id integer, submitted_time integer, ' +
           'votes integer, title text, url text)')
for l in links:
    db.execute('insert into links values (?, ?, ?, ?, ?, ?)', l)

# db is an in-memory sqlite database that can respond to sql queries using the
# execute() function.
#
# For example. If you run
#
# c = db.execute("select * from links")
#
# c will be a "cursor" to the results of that query. You can use the fetchmany()
# function on the cursor to convert that cursor into a list of results. These
# results won't be Links; they'll be tuples, but they can be passed turned into
# a Link.
#
# For example, to print all the votes for all of the links, do this:
#
# c = db.execute("select * from links")
# for link_tuple in c:
#     link = Link(*link_tuple)
#     print link.votes
#
# QUIZ - make the function query() return the number of votes the link with ID = 2 has

def query():
    c = db.execute("select * from links where id=2")
    link = Link(*c.fetchone())
    return link.votes

print query()

def query2():
    idList = []
    cursor = db.execute("select * from links where submitter_id=62443 order by submitted_time")
    for link_tuple in cursor:
        idList.append(Link(*link_tuple).id)
    return idList

def query3():
    idList = []
    cursor = db.execute("select id from links where submitter_id=62443 order by submitted_time")
    idList = [tuple[0] for tuple in cursor]
    return idList

print query2()
print query3()

## ---------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------
## ---------------------------------------------------------------------------------------------------------




