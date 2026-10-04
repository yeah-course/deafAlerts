# imports
import scipy.io.wavfile as wav
import numpy as np
import sounddevice as sd 

#sampling rate must be 16k for yamnet accuracy
fs = 16000

#recieving audio
def inputAudio():
    
    duration = 5
    print("Recording...")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    print("Done.")

    return myrecording 

rec = inputAudio()

wav.write("output.wav", fs, rec)

