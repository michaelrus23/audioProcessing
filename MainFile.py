from Signal_Processing import trackworking, plotting, writingFile

reading = 'Wav/Все струны гитары.wav'
writing = 'Wav/Result.wav'

trackSpectrum, freqs, trackProcessed, time, samplerate = trackworking(reading)

plotting(trackSpectrum, freqs, trackProcessed, time)

writingFile(trackProcessed, samplerate, writing)