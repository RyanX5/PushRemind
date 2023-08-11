# Main glue file

# An email connection establish file
# Error handler

import emailhandler
import sys
from email.mime.text import MIMEText

def run():

	_id = str(sys.argv[1])
	password = "athm heez mszu bpja"
	subject = "Go Get Your Pushups!"

	_from = "PushRemind"
	_to = "thapaswoyam123@gmail.com"

	body = "Just a very friendly reminder that you should workout! :)))"

	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = _from
	msg['To'] = _to


	handler = emailhandler.EmailHandler(_id, password, _from, _to, msg.as_string())

	handler.start()

run()