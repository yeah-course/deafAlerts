import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

rec = sd.rec(6 * 16000, samplerate=16000, channels=1, device=4, dtype="float32")
sd.wait()
print(np.max(np.abs(rec)))
rec = rec / np.max(np.abs(rec))
wav.write("test_normalized.wav", 16000, rec)
