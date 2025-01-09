import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 1, 1024, endpoint=False)
signal = np.sin(2 * np.pi * 10 * time)  # 10 Hz sine wave

fft_signal = np.fft.fft(signal)

frequencies = np.fft.fftfreq(signal.size, time[1] - time[0])

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_signal))  # We plot the absolute value for visualization
plt.title('Frequency Domain Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()