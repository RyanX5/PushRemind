# Email Handler
import smtplib



class EmailHandler:

	def __init__(self, id, password, _from, _to, content):
		self.id = id
		self.password = password
		self._from = _from
		self._to = _to
		self.content = content

	def start(self):
		

		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(self.id, self.password)
		server.sendmail(self._from, self._to, self.content)
		server.close()

		print("Email succesfully sent")

			









