import lcm
from exlcm import stark
lc = lcm.LCM("udpm://224.0.0.251:7667?ttl=1")
msg=stark()
msg.number1=20
msg.number2=80
lc.publish("Xbox", msg.encode())
