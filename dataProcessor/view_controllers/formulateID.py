from datetime import datetime

def formulate_insert_id(moduleid,iid):
	prefix = "A"
	if(moduleid==1):
		prefix = "A"
	elif (moduleid==2):
		prefix = "B"
	elif (moduleid==3):
		prefix = "C"
	elif (moduleid==4):
		prefix = "D"
	elif (moduleid==5):
		prefix = "E"
	elif (moduleid==6):
		prefix = "F"
	elif (moduleid==7):
		prefix = "G"
	elif (moduleid==8):
		prefix = "H"
	elif (moduleid==9):
		prefix = "I"
	elif (moduleid==10):
		prefix = "J"
	elif (moduleid==11):
		prefix = "K"
	elif (moduleid==12):
		prefix = "L"
	elif (moduleid==13):
		prefix = "M"
	elif (moduleid==14):
		prefix = "N"
	elif (moduleid==15):
		prefix = "O"
	elif (moduleid==16):
		prefix = "P"
	elif (moduleid==17):
		prefix = "Q"
	elif (moduleid==18):
		prefix = "R"
		
	now = datetime.now()
	dt_string = now.strftime("%d%m%Y.%H%M%S.")
	formulatedid = prefix + dt_string + iid

	return formulatedid