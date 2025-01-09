
inverse_signal = np.fft.ifft(fft_signal)
plt.plot(time, inverse_signal.real) # Take the real part as ifft may return complex numbers
plt.title('Inverse FFT - Reconstructed Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()