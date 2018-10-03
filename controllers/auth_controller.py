from controllers import mail
import random, string
from models import articles, users, admin
def sendEmail(email, isArticle):
	key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(20)])
	# check if key already exists
	while(check_key(key)):
		key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(20)])
	link = "http://coding-forum-viit.herokuapp.com/login/"
	if(isArticle):
		# Call insert in users and posts
		contents = "<h1>Hello</h1><br>Here's the link"+link+"<br>Credentials:<br>Email:"+email+"<br>Password:"+key
		try:
			mail.send_email(email,"Your Credentials", contents)
		except Exception as e:
			print("Error Sending Email. Error:"+e)
	else:
		# Call insert in users and posts
		contents = "<h1>Hello</h1><br>Here's the link"+link+"<br>Credentials:<br>Email:"+email+"<br>Password:"+key
		try:
			mail.send_email(email,"Your Credentials", contents)
		except Exception as e:
			print("Error Sending Email. Error:"+e)

def login(email, key):
	flag, admin_id = admin.check_admin_credentials(email, key)
	if(flag): #Admin
		return flag, flag, admin_id
	else:
		return False,