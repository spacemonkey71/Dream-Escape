def start():
	print """
	You went to bed in your own bedroom in your own bed. But when you wake up you find yourself on the cold hard floor of a strange room.
	The room has two doors. One of the doors is a stout wooden door. The other is made of iron.  If you open the wooden door type 'A'.
	If you open the iron door, type 'B'.
	
	next = raw_input("> ")

	if next == "left":
		itsATrap()
	elif next == "right":
		longHallway()
	elif next == "nothing":
		boredom()
	else:
		print "I didn't understand that. Please type 'left', 'right' or 'nothing'"
		
def itsATrap():
    print "As you open the door, you hear the twang of a snapping tripwire."
    print "It's the last thing you hear."
    print "GAME OVER"
    global score
    score = score - 1
    exit(0)

def boredom():
	print "This is boring."
	print "Maybe I better make another choice."
	start()
	
def longHallway():
    print "You are in a long hallway"
    print "There is a dim light at the end of the hallway"
    print "Do you go forward or turn back? Please enter 'forward' or 'back'"
    
    next = raw_input("> ")
    
    if next == "forward":
        wayOut()
    elif next == "back":
        start()
    else:
    	print "I didn't understand that."
	longHallway()

def wayOut():
	print "As you approach the end of the hallway, the light gets brighter."
	print "Soon you find yourself outside in daylight"
	print "You found the way out.  Good Job!"
	exit(0)

start()
