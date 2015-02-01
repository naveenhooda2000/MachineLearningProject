'''
Created on Jan 5, 2015

@author: nkumar2
'''
import sys
from GetFeatures import getFeaturesList

def main(argv=None):
    with open('/Users/nkumar2/Datasets/yoochoose-dataset/yoochoose-clicks-buys.session.sorted.dat', 'r') as f:
        prevstrLineList = str(f.readline()).split(',')
    listoflists = []
    sessionNumber = 1
    
    with open('/Users/nkumar2/Datasets/yoochoose-dataset/yoochoose-clicks-buys.session.sorted.dat', 'r') as f:
        for line in f:
            strLineList = str(line).split(',')
            if strLineList[0] == prevstrLineList[0]:
                listoflists.append(strLineList)
            else:
                featureList = getFeaturesList(listoflists)
                for features in featureList:
                    print features
                print "session " + str(sessionNumber + 1) + " starts, \t" + str(strLineList)
                del listoflists[:]
                sessionNumber = sessionNumber + 1
                if sessionNumber > 20:
                    break
                listoflists.append(strLineList)
            prevstrLineList = strLineList

if __name__ == "__main__":
    sys.exit(main())
