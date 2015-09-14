import csv
import datetime
from datetime import timedelta
import pprint

csvfile = open("C:\\temp\\datclicks.txt",'r')
clicksiterator = csv.reader(csvfile,delimiter="\t")
clicksiterator.next()
clicksdata = []
for row in clicksiterator:
    if row[0]<>'' and row[1]<>'' and row[2]<>'':
        row[0] = datetime.datetime.strptime(row[0],"%Y-%m-%d").date()
        if row not in clicksdata:
            clicksdata.append(row)
csvfile.close()
clicksdata.sort(key=lambda click:click[2])
print "-------------------"
csvfile = open("C:\\temp\\datsubs.txt",'r')
subsiterator = csv.reader(csvfile,delimiter="\t")
subsiterator.next()
subsdata = []
for row in subsiterator:
    if row[0]<>'' and row[3]<>'' and row[4]<>'':
        row_modified = [row[0],row[3],row[4]]
        row_modified[2] = datetime.datetime.strptime(row_modified[2],"%d-%b-%y").date()
        if row_modified not in subsdata:
            subsdata.append(row_modified)
csvfile.close()
subsdata.sort(key=lambda sub:sub[0])
print "-------------------"
#print clicksdata
#print "-------------------"
#print subsdata
#print "-------------------"
print "clicksdata length:" + str(len(clicksdata))
print "subsdata length:" + str(len(subsdata))
print "-------------------"
#print [x for x in clicksdata if len(x[2])>12]
#print [x for x in subsdata if len(x[0])>12]

output1 = []
output2 = []
for isubs in xrange(len(subsdata)):
    allclicksofasub = []
    for iclicks in xrange(len(clicksdata)):
        if clicksdata[iclicks][2] == subsdata[isubs][0] and clicksdata[iclicks][0] <= timedelta(days=1)+subsdata[isubs][2]:
            output1.append([clicksdata[iclicks][2],clicksdata[iclicks][0],clicksdata[iclicks][1],subsdata[isubs][1],subsdata[isubs][2]])
            allclicksofasub.append([clicksdata[iclicks][2],clicksdata[iclicks][0],clicksdata[iclicks][1],subsdata[isubs][1],subsdata[isubs][2]])
    allclicksofasub.sort(key=lambda click:click[1],reverse=True)
    if len(allclicksofasub) > 0:
        output2.append(allclicksofasub[0])

# print "-------------------"
# print len(output1)
# pp = pprint.PrettyPrinter(indent=1)
# pp.pprint(output1)
# print "-------------------"
# print len(output2)
# pp = pprint.PrettyPrinter(indent=1)
# pp.pprint(output2)
# print "-------------------"

output3 = {'as_gwbb1_sprime':{}, 'as_gwbb1_snoprime':{}}
output4 = {'as_gwbb1_sprime':0, 'as_gwbb1_snoprime':0}
for ioutput2 in xrange(len(output2)):
    reftag = output2[ioutput2][2]
    subsplan = output2[ioutput2][3]
    output4[reftag] += 1
    if subsplan in output3[reftag]:
        output3[reftag][subsplan] += 1
    else:
        output3[reftag][subsplan] = 1


csvfile = open("C:\\temp\\output1.txt",'w')
outputiterator = csv.writer(csvfile,delimiter="\t")
outputiterator.writerows(output1)
csvfile.close()
print "-------------------"
csvfile = open("C:\\temp\\output2.txt",'w')
outputiterator = csv.writer(csvfile,delimiter="\t")
outputiterator.writerows(output2)
csvfile.close()
print "-------------------"


pp = pprint.PrettyPrinter(indent=2)
pp.pprint(output3)
pp.pprint(output4)
print "-------------------"



