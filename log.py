import logging
#Create and configure logger 
logging.basicConfig(filename="logs/mailinglog.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='a') 

#Creating an object 
logger=logging.getLogger() 

# #Setting the threshold of logger to DEBUG 
logger.setLevel(logging.INFO) 