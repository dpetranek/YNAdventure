"""This is a text adventure. The only rule
is that every branch has to be the result
of a yes/no question. Everything else is 
fair game."""

def adventure0001():
    print "You are a dude about to have an adventure!"
    decision = raw_input("Is this awesome?")
    if decision == "yes" or decision == "y":
        print "Totally rad!"
        adventure0002()
    elif decision == "no" or decision == "n":
        print "Your right! It's totally rad."
        adventure0007()
    else:
        print "It's a yes or no question, dude."
        adventure0001()

def adventure0002():
    print "You see a time machine in your closet. It beckons with a saucy eyebrow."
    decision = raw_input("Check out the time machine?")
    if decision == "yes" or decision == "y":
        print "You decide to check it out! You approach jauntily, filled with confidence."
        adventure0003()
    elif decision == "no" or decision == "n":
        print "What happens next?"
    else:
        print "It's a yes or no question, dude."
        adventure0002()

def adventure0003():
    print "As you approach the time machine, you see that it has a toggle that indicates PAST or FUTURE and a large red button labeled GO. It is currently set to FUTURE."
    decision = raw_input("Will you press the GO button?")
    if decision == "yes" or decision == "y":
        print "Somebody knows about the first law of improv. Your vision fills with white."
        adventure0004()
    elif decision == "no" or decision == "n":
        print "What happens next?"
    else:
        print "It's a yes or no question, dude."
        adventure0004()         
            
def adventure0004():
    print "When your vision clears you see you are on a skyscraper with a sky train right next to you."
    decision = raw_input("Do you board the train?")
    if decision == "yes" or decision == "y":
        print "Let's go somewhere sunny, you think. You hop on just as the doors are closing."
        adventure0005()
    elif decision == "no" or decision == "n":
        print "What happens next?"
    else:
        print "It's a yes or no question, dude."
        adventure0004()         
            
def adventure0005():
    print "As the train speeds away at a million kilomiles an hour, you realize you don't have a ticket. A man in a uniform is headed your way."
    decision = raw_input("Do you run for it?")
    if decision == "yes" or decision == "y":
        print "You make your way away through the shiny jumpsuited crowd as inconspicuously as possible."
        #adventure0006()
    elif decision == "no" or decision == "n":
        print "What happens next?"
    else:
        print "It's a yes or no question, dude."
        adventure0005() 
        
def adventure0007():
    print "Just then, a gang of professional skateboarders enter through your window doing exotic and cool tricks."
    decision = raw_input("We're going to defeat King Eglon the Evil, bro! Join us?")
    if decision == "yes" or decision == "y":
        print "One of the skaters tosses you a sweet deck. You land on it in midair and do the best tricks."
        adventure0008()
    elif decision == "no" or decision == "n":
        print "What happens next?"
    else:
        print "It's a yes or no question, dude."
        adventure0005() 
            
def adventure0008():
    print "In formation you do tricks down the street. King Eglon is waiting in the cul-du-sac."
    decision = raw_input("Will you attempt to negotiate with him?")
    if decision == "yes" or decision == "y":
        print "Eschewing violence, you skid to a halt and ask King Eglon to renounce his evil ways."
        adventure0010()
    elif decision == "no" or decision == "n":
        print "You try to hit him with a dogwalk 620 with a backside sickie, but he makes you biff!"
        adventure0010()
    else:
        print "It's a yes or no question, dude."
    adventure0008() 

def adventure0010():
    print "He laughs in your face, then climbs aboard his rocket pogo stick and strikes down all the skaters. He then approaches you arrogantly. \"Join me and together we can rule the galaxy!\" he intones."
    decision = raw_input("Will you join him?")
    if decision == "yes" or decision == "y":
        print "You stretch out your hand and he helps you up."
        #adventure0011()
    elif decision == "no" or decision == "n":
        print "What happens next?"
    else:
        print "It's a yes or no question, dude."
        adventure0010()


adventure0001()
