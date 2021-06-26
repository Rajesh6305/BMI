#! /usr/bin/python3
import cgi
form = cgi.FieldStorage()
weight1 = form.getvalue('weight')
height1 = form.getvalue('height')
bmi = weight1/(height1*height1)
if(bmi < 18.5):
	redirectURL = "file:///C:/Users/RA20184100/OneDrive%20-%20Wipro/Documents/BMI/main.html/"
	print('<html>')
	print(' <head>')
	print('  <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />')
	print(' </head>')
	print('</html>')
