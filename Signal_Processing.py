from scipy.io import wavfile
from scipy.fft import fft, fftfreq, ifft
import numpy as np
import matplotlib.pyplot as plt
from CutSpectrum import cutExe

def trackworking(path, cut=False):

    samplerate, data = wavfile.read(path)

    try:
        print(f"number of channels = {data.shape[1]}") #количество каналов
        length = data.shape[0] / samplerate #длительность в секундах
        print(f"length = {length}s")
        time = np.linspace(0., length, data.shape[0])#массив времени

        leftChannel = data[:, 0]
        rightChannel = data[:, 1]
    except IndexError:
        print("number of channels = 1")  # количество каналов
        length = len(data) / samplerate  # длительность в секундах
        print(f"length = {length}s")
        time = np.linspace(0., length, len(data))  # массив времени
        leftChannel = data[:]

    N = len(time)
    fwd_Fourier = fft(leftChannel)
    T = time[2] - time[1]
    freqs = fftfreq(N, T) #Only positive frequencies

    if cut:
        cutExe(fwd_Fourier, freqs)

    bwd_Fourier = np.real(ifft(fwd_Fourier))

    return fwd_Fourier, freqs, bwd_Fourier, time, samplerate

def plotting(trackSpectrum, freqs, processedTrack, time):
    N = len(time)

    plt.figure(1)
    plt.plot(freqs[:N // 2], np.abs(trackSpectrum[0:N // 2]))

    plt.figure(2)
    plt.plot(time, processedTrack)
    plt.show()

def writingFile(processedTrack, samplerate, path):
    dataWrite = np.array(processedTrack)
    wavfile.write(path, samplerate, dataWrite.astype(np.int16))

