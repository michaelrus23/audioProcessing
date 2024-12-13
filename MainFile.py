from Signal_Processing import trackworking, plotting, writingFile

reading = 'Wav/LenaAAA.wav'
writing = 'Wav/Result.wav'

trackSpectrum, freqs, trackProcessed, time, samplerate = trackworking(reading, cut=True)

plotting(trackSpectrum, freqs, trackProcessed, time)

writingFile(trackProcessed, samplerate, writing)