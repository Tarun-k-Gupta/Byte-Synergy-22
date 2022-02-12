import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 8  # Setting the duration of recording
print("Listening...")

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('userSpeech.wav', fs, myrecording)  # Save as WAV file 
data, fs = sf.read('userSpeech.wav')
sf.write('userSpeech.wav', data, fs);  
