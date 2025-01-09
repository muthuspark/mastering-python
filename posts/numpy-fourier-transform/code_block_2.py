import numpy as np


#Inverse FFT
sig_recovered = np.fft.ifft(yf)

#Note:  The recovered signal will be complex.  Take the real part to get the original signal.
plt.plot(t, sig_recovered.real)
plt.show()