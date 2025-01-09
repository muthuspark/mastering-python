import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000, False)
sig = np.sin(2*np.pi*10*t) + np.sin(2*np.pi*20*t) + np.random.randn(1000)*0.5

#Compute the FFT
yf = np.fft.fft(sig)
xf = np.fft.fftfreq(sig.size, d=t[1]-t[0])

#Plot Results
plt.plot(xf, np.abs(yf))
plt.show()
