import hashlib
from hashlib import *
running = True
while running: 
	x = input("create a username")
	y = input("create a password")

	hash_object = hashlib.md5(y.encode())
	y_hashed = hash_object.hexdigest()
	#print (y_hashed)
	
	inventory = {
		x: y_hashed
	}
	
	walking = True
	while walking:
		s = input("username")
		t = input("password")
		if s == x and t == y:
			print ("you're signed in")
			running = False
			walking = False
		elif s == x and not t == y: 
			print ("incorrect password")
			running = False
		else:
			print ("create an account")
			walking = False
