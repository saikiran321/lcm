import lcm
from exlcm import xbox
lc = lcm.LCM("udpm://224.0.0.251:7667?ttl=1")
msg=xbox()
msg.message="Event(LT,205,197)"
lc.publish("Xbox", msg.encode())
