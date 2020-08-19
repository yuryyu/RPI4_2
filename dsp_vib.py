import subprocess
import numpy as np
from system_manager import *
from init import Axes_Threshold, deviation_percentage, wait_time, max_eucl
from fft_mdl import *
import time
from scipy.spatial import distance
import statistics

def vib_dsp():
   current = fft_main()
   d = distance.euclidean(current, Axes_Threshold)
   print("Euclidean distance: ",d)
   std = statistics.stdev([abs(j-i) for i,j in zip(current , Axes_Threshold)])
   print("Standard Deviation of sample is % s " 
                % (std))
   if d > max_eucl or std*100 > deviation_percentage:
      return True
   return False
   

def send2manager(client, msg2snt):
   # client - mqtt client
   tnow = time.localtime(time.time())
   msg = 'Dsp_vib Msg: ' + msg2snt + ' at ' + time.asctime(tnow)
   client.publish(sub_topic[0], msg)
   print('message ' + msg + ' sent')
   pass

if __name__ == "__main__":
   cname = "Dsp_vib-"
   client = client_init(cname)
   try:
      while conn_time == 0:
         if vib_dsp():
            send2manager(client,msg_device[0])
         time.sleep(wait_time)   
         print('send2manager procedure ended peacefully, next loop started')
   except KeyboardInterrupt:
      client.disconnect()  # disconnect from broker
      print("interrrupted by keyboard")
   finally: 
      client.disconnect()
