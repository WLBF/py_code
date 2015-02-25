#<import module> most likely will be socket, sys, but id its a web service you might import httplib, urllib,etc.
#Set up remote IP/Port variables
#Invoke the script: ./script.py <RHOST><RPORT>
RHOST = sys.argv[1]
RPORT = sys.argv[2]

#Define your buffer string that will be incremented until a potential crash
buffer = '\x41'*50

#Create a loop that will connect to the service and send the buffer:
while True:
	try:
		#send buffer
		#incerment buffer by 50
		buffer = buffer + '\x41'*50
	except:
		print "Buffer Length: "+len(buffer)
		print "Can connect to service...check debugger for potential crash"
