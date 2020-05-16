# import necessary packages
import os
from mailer import s, MY_ADDRESS
from log import logger
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from get_template import read_template
from get_contacts import get_contacts 
from get_message import writeMessage
from write_failed import cacheMessage

BASE_ASSETS_PATH = 'assets'
CONTACTS = 'contacts.txt'
MESSAGE = 'message.txt'

CONTACTS_PATH = os.path.join(BASE_ASSETS_PATH, CONTACTS)
MESSAGE_PATH = os.path.join(BASE_ASSETS_PATH, MESSAGE)

names, emails = get_contacts(CONTACTS_PATH)  # read contacts
message_template = read_template(MESSAGE_PATH)

subject = input('Type the subject')

print('\nWrite your body -   Press ctrl+c for once done', end='\n')

body = writeMessage()

for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title(), WORK_STATUS=body)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']=subject

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    try:
        s.send_message(msg)
        logger.info('sent success: {}'.format(msg))
        print('Mail Sent...')

    except Exception as e:
        res = cacheMessage(msg)
        logger.critical(e)
        print('sent failed: {},\nmsg save status: {}'.format(e, res))
    
    del msg