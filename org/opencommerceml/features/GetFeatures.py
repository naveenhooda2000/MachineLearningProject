'''
Created on Jan 31, 2015

@author: nkumar2
'''

import datetime
from operator import itemgetter
from math import floor
''' get list for all clicked items '''
def getFeaturesList(listoflists):
    purchasedItems = getItemsPurchased(listoflists)
    totalClickCount = getNumberofClickedItems(listoflists)
    featuresList = [None] * totalClickCount
    if (len(listoflists) >= 1):
        prevRecord = listoflists[0]
        index = 0
        for curRecord in listoflists[1:]:
            if len(curRecord) == 4:
                featuresList[index] = getFeatures(index, prevRecord, curRecord, purchasedItems, totalClickCount)
                index = index + 1
                prevRecord = curRecord
        featuresList[index] = getFeatures(index, prevRecord, None, purchasedItems, totalClickCount)
    return featuresList

''' get features from records'''
def getFeatures(curIndex, previousRecord, currentRecord, purchasedItems, sessionClickCount):
    features = [0, 0, 0, sessionClickCount, 0]
    features[0] = curIndex
    if currentRecord is not None:
        features[1] = int(floor(getTimeInterval(currentRecord[1], previousRecord[1])))
    else:
        features[1] = "null"
    features[2] = previousRecord[3].strip()
    if checkItemExistsInPurchased(previousRecord[2], purchasedItems):
        features[4] = 1
    return features

''' checks if the item exists in the given item list'''
def checkItemExistsInPurchased(itemId, purchasedItems):
    for purchasedItem in purchasedItems:
        if purchasedItem == itemId:
            return True
    return False

''' returns the time interval'''
def getTimeInterval(moreTime, lessTime):
    mTime = datetime.datetime.strptime(str(moreTime.replace('T', ' ').replace('Z' , '')),  '%Y-%m-%d %H:%M:%S.%f')
    lTime = datetime.datetime.strptime(str(lessTime).replace('T', ' ').replace('Z', ''), '%Y-%m-%d %H:%M:%S.%f')
    return getTimeInSeconds(mTime - lTime)

''' returns time different in seconds'''
def getTimeInSeconds(diffTime):
    #print diffTime
    curtotalSeconds = 0.0
    tokens = str(diffTime).split(':')
    curtotalSeconds = curtotalSeconds + float(tokens[0]) * 3600.0
    curtotalSeconds = curtotalSeconds + float(tokens[1]) * 60.0
    curtotalSeconds = curtotalSeconds + float(tokens[2]) * 1.0
    return curtotalSeconds

''' returns list of all items sold in the session'''       
def getItemsPurchased(listoflists):
    listoflists = sorted(listoflists, key=itemgetter(1))
    purchasedItems = []
    for curList in listoflists:
        if len(curList) == 5:
            purchasedItems.append(curList[2])
    return purchasedItems

''' number of clicked items '''
def getNumberofClickedItems(listoflists):
    clickCount = 0
    for curList in listoflists:
        if len(curList) == 4:
            clickCount = clickCount + 1
    return clickCount