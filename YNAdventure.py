"""This is a text adventure. The only rule
is that every branch has to be the result
of a yes/no question. Everything else is 
fair game."""

def adventure0001():
	print "You are a dude about to have an adventure!"
	decision = raw_input("Is this awesome?")
	if decision == "YES" or decision == "Yes" or decision == "yes":
		print "Totally rad!"
		adventure0002()
	elif decision == "NO" or decision == "No" or decision == "no":
		print "Game over an account of poor decision making."
	else:
		print "It's a yes or no question, dude."
		adventure0001()

def adventure0002():
	print "You see a time machine in your closet. It beckons with a saucy eyebrow."
	decision = raw_input("Check out the time machine?")
	if decision == "YES" or decision == "Yes" or decision == "yes":
		print "You decide to check it out! You approach jauntily, filled with confidence."
		adventure0003()
	elif decision == "NO" or decision == "No" or decision == "no":
		print "Game over an account of poor decision making."
	else:
		print "It's a yes or no question, dude."
		adventure0002()

def adventure0003():
	print "As you approach the time machine, you see that it has a toggle that indicates PAST or FUTURE and a large red button labeled GO. It is currently set to FUTURE."
	decision = raw_input("Will you press the GO button?")
	if decision == "YES" or decision == "Yes" or decision == "yes":
		print "Somebody knows about the first law of improv. Your vision fills with white."
		adventure0004()
	elif decision == "NO" or decision == "No" or decision == "no":
		print "Game over an account of poor decision making."
	else:
		print "It's a yes or no question, dude."
		adventure0004()			
			
def adventure0004():
	print "When you're vision clears you see you are on a skyscraper with a train right next to you."
	decision = raw_input("Do you board the train?")
	if decision == "YES" or decision == "Yes" or decision == "yes":
		print "Let's go somewhere sunny, you think. You hop on just as the doors are closing."
		adventure0005()
	elif decision == "NO" or decision == "No" or decision == "no":
		print "Game over an account of poor decision making."
	else:
		print "It's a yes or no question, dude."
		adventure0004()			
			
def adventure0005():
	print "As the train speeds away at a million kilomiles an hour, you realize you don't have a ticket. A man in a uniform is headed your way."
	decision = raw_input("Do you run for it?")
	if decision == "YES" or decision == "Yes" or decision == "yes":
		print "You make your way away through the jumpsuited crowd as inconspicuously as possible."
		#adventure0006()
	elif decision == "NO" or decision == "No" or decision == "no":
		print "Game over an account of poor decision making."
	else:
		print "It's a yes or no question, dude."
		adventure0005()	
			
adventure0001()
