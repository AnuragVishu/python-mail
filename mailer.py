# import the smtplib module. It should be included in Python by default
import smtplib
from log import logger 
from getpass import getpass

MY_ADDRESS = input('Enter email: ')
PASSWORD = getpass('Enter Password: ')

try:
    print('Establishing SMTP connection...')
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    print('logging in to: {}'.format(MY_ADDRESS))
    s.login(MY_ADDRESS, PASSWORD)
    print('success..',end='\n')
    
    logger.info('ID {} logged-in'.format(MY_ADDRESS))

except Exception as e:
    logger.critical(e)
    print('Error: ',e)
