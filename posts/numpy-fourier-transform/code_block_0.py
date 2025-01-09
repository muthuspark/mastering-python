import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000, False)  # 1 second
sig = np.sin(2*np.pi*10*t) # 10 Hz signal

#Compute the FFT
yf = np.fft.fft(sig)
xf = np.fft.fftfreq(sig.size, d=t[1]-t[0])

#Plot the results.  Note that the FFT produces complex numbers. We take the absolute value to get the magnitude.
plt.plot(xf, np.abs(yf))
plt.show()