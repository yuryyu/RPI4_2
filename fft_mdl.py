import matplotlib.pyplot as plt
import numpy as np
from data_acq import *


Fs = 2048.0  # sampling rate
Ts = 1.0/Fs # sampling interval
#t = np.arange(0,1,Ts) # time vector

data = acq_data()
Xdata = data.AxisX.to_numpy()
Ydata = data.AxisY.to_numpy()
Zdata = data.AxisZ.to_numpy()

t = np.arange(0,len(Xdata)/Fs,Ts) # time vector
#ff =12   # frequency of the signal
#y = np.sin(2*np.pi*ff*t)


y = Xdata - np.mean(Xdata)

n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
print(range(int(n/2)))
frq = frq[range(int(n/2))] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(int(n/2))]
thrh=np.mean(abs(Y))
fig, ax = plt.subplots(2, 1)
ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[1].plot(frq,abs(Y),'b',frq,thrh+abs(Y)*0,'r') # plotting the spectrum
ax[1].vlines([180, 200, 600,620], 0, np.max(abs(Y)),  colors='r')
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
ax[0].grid(True)
ax[1].grid(True)
print('End of FFT script!')
#plt.savefig('data/AxisX.png')
plt.show()