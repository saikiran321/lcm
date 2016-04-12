import lcm
from exlcm import stark
def  iron_msg(channel,data):
	msg=stark.decode(data)
	print("Hi incoming message on channel %s" %channel)
	total=msg.number1+msg.number2	
	print("Total %d" %total)
	print("")
lc=lcm.LCM()
subscribe=lc.subscribe("iitm",iron_msg)

try :
	while True:
		lc.handle()
except KeyboardInterrupt:
	pass
