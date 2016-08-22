def everyone_sign():
	names = ['Diane', 'Danica', 'Danielle', 'Glenda', 'Leon']
	msg = {}

	for i in range(0, len(names)):
		if i == 0:
			msg[names[i]] = "Thank you! Your friends: " + ", ".join(names[i+1:len(names)])
		else:
			msg[names[i]] = "Thank you! Your friends: " + ", ".join(names[0:i]) + ", " + ", ".join(names[i+1:len(names)])	
		
	print msg		

everyone_sign()