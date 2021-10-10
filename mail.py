import smtplib
smail='sunilktm1999@gmail.com'
rmail=['rajaktm1999@gmail.com']
msg="""From: From Person %s
To:To Person %s 
Subject:Sending SMTP e-mail
This is test e-mail message."""%(smail,rmail)
try:
	password=input('Enter password -');
	smtpobj=smtplib.SMTP('gmail.com',587)
	smtpobj.login(smail,password)
	smtp.sendmail(smail,rmail,msg)
	print("Successful send the mail")
except Exception:
	print("Error: to send mail ")