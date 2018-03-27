def start():
	print """
	You went to bed in your own bedroom in your own bed. But when you wake up you find yourself on the cold hard floor of a strange room. There is a trilobite on the floor with you.
	"""
	print ""
	print"....~..........................................................................."
	print"......D=...............................N............88I........................."
	print"........~N8..............................8D.............88......................"
	print"...........DDN.............................DD.............I,,..................."
	print".............=NDD............................DD..............Z8................."
	print"................NNN............................ND........88....~=..............."
	print"..................ONNN...........................D+.........DN..D8.............."
	print".....................DNN=.........................OD..........DD..D............."
	print".......................DNND$?..M+7?:::,............ID..........ZN.,N............"
	print".........................+Z7O$,8Z7DID7+IO7+DIIO8,.7OZ$,,,,......8N..N,.........."
	print"..........................,DZI$77I~I$?$?ID7=7$$877ZIZ$$.,,,,....=N,,OM,,........"
	print"...........................++7IOZ$7Z7$I$IIOIOI778ZZ7I78DDNN,,,..8N.,,8,,,,,,...."
	print"..........................OOOZII77ZOO77I$IIZ78I$+$D8I8ZZ78Z$ZZ8ODN...ON,,,,,,..."
	print".........................O8NZ$O,Z.?I87O$8$O$8~OI$7$8D+$87$ZZOODDZ....ID,,:,,,,,,"
	print"..........................8+ZZ777?.:,I7$I8ZO7O$Z?ZD7$$7O8$ZOO8D8$,,,,,D,,:::,,,,"
	print"........................Z=DNNND?~..~7$8~$7?ZZ$Z77D?$Z7Z?$OD7DD8DZ::,,+D,,,:,,,,,"
	print"..........................7~OZIZ7?$NI$$$7$Z+87D$8$Z8$$7ZOODDZND8D7=~:Z8::::,,,,,"
	print"..........................~.?D:OOIO=8I7$ZZ77$ZZ$$OOZZO$OZ88$$O$DD$OZ$D7?=~:,,,,,"
	print"............................O8DNDDD$I+OO$:II7O8?O$$$$ZZO8D?$$ZO87888O88$=~:,,,,,"
	print".......M8...................=OO8DNINDDO$~7IID8$Z+$Z78ZZ88D$$$Z8DDNNN88O$+~::,,,,"
	print"..........8NND$..............DZ788Z8O$ND$$8DD$$$$ZZ$ZDNNDOZZO8DNNO888OOZ?=~:,,,,"
	print"..............,DNNNND7........,Z8ZZZZOZ$$NDD$Z:$$$ZZZOOOOOOO8DDD8D88OOOO7==~::::"
	print"....................IDNNNNNNNNNNDO8DNNNNDNNZ8ND$$Z$OOZOO8O88DDDDDD8O8OOO$++==~~~"
	print"...............................N8DD88DD8DDDZ8Z8NNDZOZO8DDDDDDDDDDD8888OOOZ7I+=~~"
	print"..................,,,,,,,,.......,O87.,:DN$NZ8OOOODNNND8DNDNDDDDD8888O88OZI+=~::"
	print"...................,,,,,,,,,,,,,,,D,:+7NNINN$8OZ88ODDN8NNNDDNDDDDD8888888O7++=~:"
	print",...................,,,,,,::::::::::,ZNNDDNN$DD8NDNDNNNNNNNNDDDDD88888888Z7?==~:"
	print",...,....,............,,,,,,,,::::~~~~~~NN=NDDNDNND8NDDNNNNDDDDD88888OZ$I?=~~:::"
	print",,,,,,,,,,..,.....,...ONN.,,,,,,,,,,,,:,NNNND~:ON$D8D8$8DDDDDDDD888Z7I+=~:::::,,"
	print",,,,,,,,,,,,,,,,,,,,.,,,,:NNNNNDDNNNNNNND,,,,,,.O~,,I8~=I$OO88OZ777I==~~::,,,,,,"
	print",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,,,,,,,,,,,,,,,,:~=?7ZZ7I+=~~~=~~~:::::,,,:"
	print",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,::~=++++=~~::::~~::~~:::::,,"
	print ""
	print """
	The room has two doors. One of the doors is a stout wooden door. The other is made of iron.  If you open the wooden door type 'A'.
	If you open the iron door, type 'B'.

	"""
	
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
