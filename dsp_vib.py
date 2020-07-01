import subprocess
import numpy as np
from system_manager import *

import time


def vib_dsp():
   pass


def send2manager(client, msg2snt):
   # mqtt client
   tnow = time.localtime(time.time())
   msg = 'Dsp_vib Msg: ' + str(msg_device[0]) + ' at ' + time.asctime(tnow)

   client.publish(sub_topic[0], msg)
   print('message ' + msg + ' sent')
   pass

if __name__ == "__main__":
   cname = "Dsp_vib-"
   client = client_init(cname)
   try:
      while conn_time == 0:
         if vib_dsp():
            send2manager(client,msg_device[3])
         print('send2manager procedure ended peacefully, next loop started')
   except KeyboardInterrupt:
      client.disconnect()  # disconnect from broker
      print("interrrupted by keyboard")
   finally: 
      client.disconnect()
