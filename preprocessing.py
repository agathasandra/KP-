#Sources:
#https://stackoverflow.com/questions/46614526/how-to-import-a-csv-file-into-a-data-array
#https://stackoverflow.com/questions/25191620/creating-lowpass-filter-in-scipy-understanding-methods-and-units

import csv
import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

#deklarasi Array
data1 = [0]*60000

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data1, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data1)
    return y

# Filter requirements.
order = 6
fs = 30.0       # sample rate, Hz
cutoff = 3.667  # desired cutoff frequency of the filter, Hz

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, fs, order)

# Plot the frequency response.
w, h = freqz(b, a, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()

# Data to be filtered.
#Data Requirements
T = 2000.0         # seconds
n = int(T * fs) # total number of samples
t = np.linspace(0, T, n, endpoint=False)

#mengubah CSV ke array
with open('bidmc_01_Signals.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
    for x in range (len(data) -2):
        data1[x] = float(data[x+1][2])

# Filter the data, and plot both the original and filtered signals.
y = butter_lowpass_filter(data1, cutoff, fs, order)

plt.subplot(2, 1, 2)
plt.plot(t, data1, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()
