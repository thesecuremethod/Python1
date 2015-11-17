from sys import exit

def firstRoom(): 
    print "Yay!" 
    exit(0) 

def start(): 
	print "Welcome! You have stumbled into the dungeon of development!"
#  play sound --  
	print "Here you will have to learn to write code that executes well. Good luck!" 
	print "" 
	print "There are three doors in the room you are in, each labeled with a language type and a lit candle next to the door. One says 'JavaScript, the next is 'Python', and the last is 'Ruby'. A placard on the floor says, 'Choose your path and disable all other system resources before moving forward'."

	js_candle_lit = True
	rb_candle_lit = True

	print ""
	print "What do you do?"

	while True: 
	
		choice = raw_input("> ") 

		if choice == "open JavaScript door": 
			print "The door doesn't budge. Maybe youre not here for JS...."

		elif choice == "open Python door" and js_candle_lit and rb_candle_lit: 
			print "You need to disable other system resources first."

		elif choice == "open Python door" and not js_candle_lit and rb_candle_lit:
				print "The door needs a little more power to open...."
 
		elif choice == "open Python door" and js_candle_lit and not rb_candle_lit:
				print "The door needs a little more power to open...." 

		elif choice == "open Python door" and not js_candle_lit and not rb_candle_lit:
				print "The Python door opens...." 
				print "Good Job!" 
				firstRoom() 
 
		elif choice == "open Ruby door": 
			print "The door doesn't budge. Maybe youre not here for Ruby..."
 
		elif choice == "js_candle.blowout()": 
			print "The Python candle seems to glow a little brighter..." 
			js_candle_lit = False
		elif choice == "rb_candle.blowout()": 
			print "The Python candle seems to glow a little brighter..." 
			rb_candle_lit = False 
		else:   print "Thats not valid input for this program. Learn about case sensitivity or take up tennis." 
 


#choice = raw_input("> ")
	
#	if choice == "left": 
#		bear_room()
#	elif choice == "right": 
#		cthulhu_room()
#	else: 
#		dead("You stumble and die.")
start()
 
