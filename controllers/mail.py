#! /usr/local/bin/python


import sys
import os
import re

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

def send_email(destination, subject, content):
	SMTPserver = 'smtp.gmail.com'
	sender =  os.environ['EMAIL_ID']
	# destination = ['test@test.com']

	USERNAME = os.environ['EMAIL_ID']
	PASSWORD = os.environ['EMAIL_PASSWORD']

	# typical values for text_subtype are plain, html, xml
	text_subtype = 'plain'

	subject="Your Credentials"


	try:
		msg = MIMEText(content, text_subtype)
		msg['Subject'] = subject
		msg['From'] = sender # some SMTP servers will do this automatically, not all

		conn = SMTP(SMTPserver)
		conn.set_debuglevel(False)
		conn.login(USERNAME, PASSWORD)
		try:
			conn.sendmail(sender, destination, msg.as_string())
		finally:
			conn.quit()

	except Exception as exc:
		sys.exit( "mail failed; %s" % str(exc) ) # give a error message
