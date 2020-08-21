
import socket

# Common
conn_time = 0 # 0 stands for endless loop

# MQTT broker init data
nb=0 # 0- HIT-"139.162.222.115", 1 - open HiveMQ - broker.hivemq.com
brokers=[str(socket.gethostbyname('vmm1.saaintertrade.com')), str(socket.gethostbyname('broker.hivemq.com'))]
ports=[80,1883]
usernames = ['MATZI',''] # should be modified for HIT
passwords = ['MATZI',''] # should be modified for HIT
broker_ip=brokers[nb]
port=ports[nb]
username = usernames[nb]
password = passwords[nb]

mzs=['matzi/','']
ext_man = mzs[nb]+'system/command'
sub_topic = [mzs[nb]+'bearer/accel/status', mzs[nb]+'bearer/belt/status']
pub_topic = mzs[nb]+'system/state'
msg_system = ['Vibration exceed norma!', 'Belt issue!','No issue detected, PASS.']
wait_time = 5

# FFT module init data
isplot = False
issave = False

# DSP init data
percen_thr=0.05 # 5% of max energy holds
Fs = 2048.0
Axes_Threshold = [1.3, 0.9, 1.0] #[1.5915293857758341, 0.7518114801870276, 1.137742491864477]#
deviation_percentage = 10
max_eucl = 0.5 

# Acq init data
is_glink = True
onboard = False
acqtime = 10.0 # sec

# DB init data 
db_name = 'data\\K544.db' # SQLite
db_init = False # True if we need calibrate setup