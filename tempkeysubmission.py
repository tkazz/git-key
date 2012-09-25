#!/Python27/python
import smtplib
import cgi
import sys
import cgitb
osVersion = sys.platform
#instantiate FieldStorage.
form = cgi.FieldStorage()
timesheetVersion = form.getvalue('tsversion')
customerName = form.getvalue('customer')
email = form.getvalue('email')
operatingSystem = form.getvalue('operatingsystem')
numberofUsers = form.getvalue('users')
date = form.getvalue('date')
quickBooks = form.getvalue('quickbooks')
msp = form.getvalue('msp')
px = form.getvalue('px')
rl = form.getvalue('reportlink')
addText = form.getvalue('textarea')
print "Content-type: text/html; charset=utf-8"
print
print '<HTML><HEAD><TITLE>Form Submitted</TITLE><link href="/tempkeystyle.css" rel="stylesheet" type="text/css"/>'
print '<link rel="shortcut icon" href="/key2.ico" type="image/x-icon" /></HEAD>'
print '<body>'
print '<div id="sitebranding">'
print '<h1>Your request was submitted.</h1>'
print '</div>'
print '<div id="main_submit">'
print '<p style="font-weight:bold">'
print '<div id="submitted">'
print '<p id="centered">'
print 'You submitted the following request to troykacz@gmail.com'
print '</p>'
print '<br />'
print '<div class="blockstuff">'
print 'Your Email :'
print '</div>'
print '<div class="formfield">'
print email
print '</div>'
print '<div class="blockstuff">'
print 'Version of Timesheet: '
print '</div>'
print '<div class="formfield">'
print timesheetVersion
print '</div>'
print '<div class="blockstuff">'
print 'Customer: '
print '</div>'
print '<div class="formfield">'
print customerName
print '</div>'
print '<div class="blockstuff">'
print 'Operating System: '
print '</div>'
print '<div class="formfield">'
print operatingSystem
print '</div>'
print '<div class="blockstuff">'
print 'Number of users: '
print '</div>'
print '<div class="formfield">'
print numberofUsers
print '</div>'
print '<div class="blockstuff">'
print 'Date license expires: '
print '</div>'
print '<div class="formfield">'
print date
print '</div>'
if quickBooks == None:
	pass
else:
	print '<div class="blockstuff">'
	print "Quickbooks" 
	print '</div>'
	print '<div class="formfield">'
	print "Yes"
	print '</div>'
if msp == None:
	pass
else: 
	print '<div class="blockstuff">'
	print "Projectlink" 
	print '</div>'
	print '<div class="formfield">'
	print "Yes"
	print '</div>'
if px == None:
	pass
else: 
	print '<div class="blockstuff">'
	print "ProjectXecute"
	print '</div>'
	print '<div class="formfield">'
	print "Yes"
	print '</div>'
if rl == None:
	pass
else:
	print '<div class="blockstuff">'
	print "Reportlink"
	print '</div>'
	print '<div class="formfield">'
	print "Yes"
	print '</div>'
if addText == None:
	pass
else:
	print '<div class="blockstuff">'
	print 'Additional comments: '
	print '</div>'
	print '<div class="formfield">'
	print addText
	print '</div>'
print '<br />'
print '<p align="center">'
print 'Click <a style="color:red" href="/tempkey.html">right here</a> to return to the request page.</p>'
print '</div>'
print '</div>'
print '<br>'
###################################
#email the form results           #
###################################
TO = ["troykacz@gmail.com"]
FROM = '%s' % email
email_user = 'user_name_here'
email_password = 'user_password_here'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(user_name_here, user_password_here)
subject = "Temp Key Request"
body = '\n' + 'Version: ' + str(timesheetVersion) + '\n' + 'Customer: ' + str(customerName) + '\n' + 'OS: ' + str(operatingSystem) + '\n' + 'Users: ' + str(numberofUsers) + '\n' + 'Date: ' + str(date)
if quickBooks == None:
	pass
else:
	body += '\n' + 'Quickbooks'
if msp == None:
	pass
else:
	body += '\n' + 'Microsoft Project'
if px == None:
	pass
else:
	body += '\n' + 'ProjectXecute'
if rl == None:
	pass
else:
	body += '\n' + 'Reportlink'
if addText == None:
	pass
else:
	body += '\n\n' + 'Additional Comments:\n%s' % str(addText)
message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), subject, body)
smtpserver.sendmail(FROM, TO, message)
smtpserver.close()
print '<div>'
print '</BODY>'