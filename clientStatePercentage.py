#!/usr/bin/python
#encoding:utf-8

try:
	import sys,optparse
except:
	print("Error running 'import sys,optparse'. Maybe you have to install some python library")

def clientStatePercentage(logfile,state):
	try:
		contents = open(logfile, "r")
	except IOError, e:
		print 'Error openning file '+ logfile +": "+e.strerror
		raise
	except:
		print 'Error openning file '+ logfile
		raise
	totalRequests = 0
	requests = 0
	for line in contents:
		totalRequests += 1
		if line.split(" ")[8] == state:
			requests += 1
	return int(0.5+float(100*requests)/totalRequests)

parser = optparse.OptionParser("usage%prog " + "[-f <file>] [-e HTTP STATE[,HTTP_STATE2,[...]]]")
parser.add_option('-f', dest = 'file', type = 'string', help = 'Please, specify the Apache access file', default="/var/log/apache2/access.log")
parser.add_option('-e', dest = 'state', type = 'string', help = 'Please, specify the HTTP State', default="304")
(options, args) = parser.parse_args()
log=options.file
states=options.state.split(',')

for state in states:
	print 'Percentage of requests with ' + state + ' state: ' + str(clientStatePercentage(log,state)) + '%'


