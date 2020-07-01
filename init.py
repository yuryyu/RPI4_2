
import socket

nb=0 # 0- HIT-"139.162.222.115", 1 - open HiveMQ - broker.hivemq.com
brokers=[str(socket.gethostbyname('vmm1.saaintertrade.com')), str(socket.gethostbyname('broker.hivemq.com'))]
ports=[80,1883]
usernames = ['',''] # should be modified for HIT
passwords = ['',''] # should be modified for HIT
broker_ip=brokers[nb]
port=ports[nb]
username = usernames[nb]
password = passwords[nb]
conn_time = 0 # 0 stands for endless
mzs=['matzi/','']
sub_topic = [mzs[nb]+'bearer/accel/status', mzs[nb]+'bearer/belt/status']
msg_device = ['detected']
pub_topic = mzs[nb]+'system/state'
msg_system = ['Vibration exceed norma!', 'Belt issue!']
