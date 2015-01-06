'''
Created on Jan 5, 2015

@author: nkumar2
'''
import sys, datetime

from operator import itemgetter

def main(argv=None):
    with open('/Users/nkumar2/Datasets/yoochoose-clicks-buys.session.sorted.dat', 'r') as f:
        prevstrLineList = str(f.readline()).split(',')
    listoflists = []
    sessionNumber = 1
    with open('/Users/nkumar2/Datasets/yoochoose-clicks-buys.session.sorted.dat', 'r') as f:
        for line in f:
            strLineList = str(line).split(',')
            if strLineList[0] == prevstrLineList[0]:
                listoflists.append(strLineList) 
            else:
                (totalclickCount, totalClickTime, purchaseCount) = printClickTimeIntervals(listoflists)
                print str(listoflists[0][0]) +","+ str(totalclickCount) +","+ str(totalClickTime) +","+ str(purchaseCount)
                del listoflists[:]
                sessionNumber = sessionNumber + 1
                if sessionNumber > 20:
                    break
                listoflists.append(strLineList)
            prevstrLineList = strLineList

def getTimeInSeconds(diffTime):
    #print diffTime
    curtotalSeconds = 0.0
    tokens = str(diffTime).split(':')
    curtotalSeconds = curtotalSeconds + float(tokens[0]) * 3600.0
    curtotalSeconds = curtotalSeconds + float(tokens[1]) * 60.0
    curtotalSeconds = curtotalSeconds + float(tokens[2]) * 1.0
    return curtotalSeconds

def printClickTimeIntervals (listoflists):
    haspurchased = 0
    clickCount = 0
    purchaseCount = 0
    totalTimeInSeconds = 0.0
    if (len(listoflists) > 1):
        prevList = listoflists[0]
        for curList in listoflists[1:]:
            if len(curList) == 4 and haspurchased == 0:
                prevTime = datetime.datetime.strptime(str(prevList[1]).replace('T', ' ').replace('Z', ''), '%Y-%m-%d %H:%M:%S.%f')
                curTime = datetime.datetime.strptime(str(curList[1].replace('T', ' ').replace('Z' , '')),  '%Y-%m-%d %H:%M:%S.%f')
                totalTimeInSeconds = totalTimeInSeconds +  getTimeInSeconds(curTime - prevTime)
                clickCount = clickCount + 1
            elif len(curList) == 5:
                #print "purchase " + str(curList)
                haspurchased = 1
                purchaseCount = purchaseCount + 1
            else:
                print "Exiting purchased and then clicked"
                sys.exit(1)
            prevList = curList
     
    return (clickCount, totalTimeInSeconds, purchaseCount)

'''       
def getItemSoldCountAndTimeDiff(listoflists):
    listoflists = sorted(listoflists, key=itemgetter(1))
    clickCount = 0
    purchaseCount = 0
    for curList in listoflists:
        if len(curList) == 4:
            clickCount = clickCount + 1
        if len(curList) == 5:
            purchaseCount = purchaseCount + 1
            
    print "For Session "+str(listoflists[0][0])+" => Click Count " + str(clickCount) +", Purchase Count " + str(purchaseCount)
    return (clickCount, purchaseCount)
'''

if __name__ == "__main__":
    sys.exit(main())
