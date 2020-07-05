import matplotlib.pyplot as plt
import numpy as np
from data_acq import *
from init import isplot, issave


def thrh_comp(Y):
    ''' Used for Dynamic Threshold calculation and therein carries scattered energy info'''
    percen_thr=0.05 # 5% of max energy holds
    return np.mean(np.sort(abs(Y))[-int(len(Y)*percen_thr):-1])
 

def fft_block(Xdata, isplot, issave, fname='data/AxisX_pass.png'):
    Fs = 2048.0  # sampling rate
    Ts = 1.0/Fs # sampling interval
    t = np.arange(0,len(Xdata)/Fs,Ts) # time vector
    y = Xdata - np.mean(Xdata)
    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range    
    frq = frq[range(int(n/2))] # one side frequency range
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]    
    thrh=thrh_comp(Y)
    if isplot:
        fig, ax = plt.subplots(2, 1)
        ax[0].plot(t,y)
        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Amplitude')
        ax[1].plot(frq,abs(Y),'b',frq,thrh+abs(Y)*0,'r') # plotting the spectrum
        ax[1].vlines([230, 240 ], 0, np.max(abs(Y)),  colors='g')
        ax[1].vlines([ 470, 480 ], 0, np.max(abs(Y)),  colors='g')
        ax[1].vlines([ 710, 720 ], 0, np.max(abs(Y)),  colors='g')
        ax[1].vlines([ 565, 630 ], 0, np.max(abs(Y)),  colors='g')
        ax[1].set_xlabel('Freq (Hz)')
        ax[1].set_ylabel('|Y(freq)|')
        ax[0].grid(True)
        ax[1].grid(True)
        if issave:
            plt.savefig(fname)        
        plt.show()
    return thrh*10000    

def fft_main(fname = "data/data_good.csv"):
    data = acq_data(fname)
    datapool=[  data.AxisX.to_numpy(),
                data.AxisY.to_numpy(),
                data.AxisZ.to_numpy()]
    Ax_thrh=[]
    for cnt, Xdata in enumerate(datapool):
        Ax_thrh.append(fft_block(Xdata, isplot, issave, fname='data/Axis'+str(cnt)+'.png'))
    return Ax_thrh


if __name__ == "__main__":    
    print( fft_main("data/data_good.csv"))   
    