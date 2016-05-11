import lcm
from exlcm import xbox
lc=lcm.LCM()
msg=xbox()
msg.message="Event(LT,205,197)"
lc.publish("Xbox", msg.encode())
