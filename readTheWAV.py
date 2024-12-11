from scipy.io import wavfile
from scipy.fft import fft, fftfreq, ifft
import matplotlib.pyplot as plt
import numpy as np
from CutSpectrum import cutExe

samplerate, data = wavfile.read('MyVoice.wav')

print(f"number of channels = {data.shape[1]}") #количество каналов
length = data.shape[0] / samplerate #длительность в секундах
print(f"length = {length}s")
time = np.linspace(0., length, data.shape[0]) #массив времени
print(time)

leftChannel = data[:, 0]
rightChannel = data[:, 1]

N = len(time)
trackSpectrum = fft(leftChannel)
T = time[2] - time[1]
freqs = fftfreq(N, T) #Only positive frequencies
plt.plot(freqs[:N//2], np.abs(trackSpectrum[0:N // 2]))
plt.show()

# cutExe(trackSpectrum, freqs)
# plt.plot(freqs[:N//2], np.abs(trackSpectrum[0:N // 2]))
# plt.show()

processedTrack = np.real(ifft(trackSpectrum))
plt.plot(time, processedTrack)
plt.show()

dataWrite = np.array(processedTrack)
wavfile.write("CutBegin.wav", samplerate, dataWrite.astype(np.int16))