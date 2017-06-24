#!shebang

import time,sys 
startTime = time.time()
sys.path.append('~/.Private/scriptFiles/python')
import twitterToMongoSetup as setup
import pymongo,datetime,signal 

print "It took %s to do imports and start logging." % str(datetime.timedelta(seconds=time.time()-startTime))

class gracefulShutdown():
    def __init__():
        
