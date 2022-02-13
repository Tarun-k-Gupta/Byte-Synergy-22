import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import GUI

def botListen():
    fs = 44100  # Sample rate
    seconds = 8  # Setting the duration of recording
    GUI.botSpeak("I am listening")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write('userSpeech.wav', fs, myrecording)  # Save as WAV file 
    data, fs = sf.read('userSpeech.wav')
    sf.write('userSpeech.wav', data, fs);  
