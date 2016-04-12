import lcm
from exlcm import stark
lc = lcm.LCM()
msg=stark()
msg.number1=20
msg.number2=80
lc.publish("iitm", msg.encode())
