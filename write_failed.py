import os 
from datetime import datetime
from log import logger

CACHE_DIR = 'assets/cache'

def getTimeStamp():
    timestamp = 1545730073
    dtm = datetime.fromtimestamp(timestamp)
    return dtm

def cacheMessage(msg):
    ts = getTimeStamp()
    cache = open(os.path.join(CACHE_DIR,"msg"+str(ts)+".txt"),"w") 

    try:
        cache.writelines(msg) 
        cache.close() 
        logger.info('WRITE CACHE SUCCESS')
        return True
    except Exception as e:
        logger.exception('WRITE CACHE FAILED: {}'.format(e))
        return e
