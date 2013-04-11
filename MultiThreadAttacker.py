#!/usr/bin/python

#assume that 5 thread to use

import socket;
import threading;

class AttrackerThread(threading.Thread):
	
	threadID = 0;
	password = 0;
	servAddr = 0;
	servPort = 0;
	
	#Initiate the thread.
	def __init__(self,threadID, passwrds, servaddr,servport):
		threading.Thread.__init__(self);
		self.threadID = threadID;
		self.password = passwrds;
		self.servAddr = servaddr;
		self.servPort = servport;

#	#Fetch the its own part passwords from the the 'passwords' string list Given by Caller.
#	def fetchPasswords(passs):
#		passwords = passwrds;
#		print 'Fetch' + len(passwords) + 'password record successfully';
#		return;

	#Start to try every password in the 'passwords'.
	def startAttack(self):
		for index in range(len(passwords)):
			print self.threadID + ':' + index +'th password.';
			clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
			clientSocket.connect((serveripaddr, serverpors));
			clientSocket.send('Samuel '+passwords[index]);
			authInfo = clientSocket.recv(100);
			if authInfo =='OK':
				print 'Find Successful:' + passwords[index];
				break;
		print 'Finish but no Answer';
		return;

	#Overrided run function
	def run(self):
		print 'Starting:' + self.threadID;
#		fetchPassword();
		startAttack();
		print 'Stop:' + self.threadID;

# fetch the file<./PasswordDictionary.txt" and parse it into N string lists.
def fetch():
	fileReader = open("PasswordDictionary.txt");
	rawPasswords = fileReader.read();
	passwordList = 	rawPasswords.split('\n');
	lengthPasswordList = len(passwordList);
	print len(passwordList);
	passwordlist1 = passwordList[:lengthPasswordList/5];
	passwordlist2 = passwordList[lengthPasswordList/5+1:2*lengthPasswordList];
	passwordlist3 = passwordList[2*lengthPasswordList/5+1:3*lengthPasswordList];
	passwordlist4 = passwordList[3*lengthPasswordList/5+1:4*lengthPasswordList];
	passwordlist5 = passwordList[4*lengthPasswordList/5+1:];

	return ( passwordlist1,passwordlist2, passwordlist3, passwordlist4, passwordlist5); 
#Main Function is here
passwrd1, passwrd2, passwrd3, passwrd4, passwrd5 = fetch();

thread1 = AttrackerThread('Thread001',passwrd1,'localhost',12345);
thread1.start();

thread2 = AttrackerThread('Thread002',passwrd1,'localhost',12345); 
thread2.start();

thread3 = AttrackerThread('Thread003',passwrd1,'localhost',12345);
thread3.start();

thread4 = AttrackerThread('Thread004',passwrd1,'localhost',12345); 
thread4.start();

thread5 = AttrackerThread('Thread005',passwrd1,'localhost',12345); 
thread5.start();
