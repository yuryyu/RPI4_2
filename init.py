
import socket

# MQTT broker init data
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
wait_time = 5

# FFT module init data
isplot = False
issave = False

# DSP init data
percen_thr=0.05 # 5% of max energy holds
Fs = 2048.0
Axes_Threshold = [1.3, 0.9, 1.0] #[1.5915293857758341, 0.7518114801870276, 1.137742491864477]#
deviation_percentage = 15
max_eucl = 0.5 

# Acq init data
onboard = True

# DB init data 
db_name = 'data\\K544.db' # SQLite
db_init = False # True if we need calibrate setup