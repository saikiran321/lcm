import lcm
from exlcm import xbox
def  iron_msg(channel,data):
	msg=xbox.decode(data)
	print "Hi incoming message on channel %s" %channel
	print msg.message
	print("")
lc=lcm.LCM("udpm://224.0.0.251:7667?ttl=1")
subscribe=lc.subscribe("Xbox",iron_msg)

try :
	while True:
		lc.handle()
except KeyboardInterrupt:
	pass
