# setup
audioFile = "sample-file-4.wav"
newAudioFile = "new_audio.wav"
mashAudioFile = "mash.wav"
import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

# analyze .wav file
obj = wave.open(audioFile, 'r')
print("Number of channels", obj.getnchannels())
print("Sample Width", obj.getsampwidth())
print("Frame Rate", obj.getframerate())
print("Number Frames", obj.getnframes())
print("Parameters", obj.getparams())
frames = obj.readframes(obj.getnframes())
print("Sample Frames", frames[0:5])
obj.close()

# display .wav file
obj2 = wave.open(audioFile, 'rb')
raw = np.frombuffer(obj2.readframes(-1), np.int16)
plt.plot(raw, color='blue')
plt.show()
obj2.close()

# write .wav file
frame_rate = 88200
obj3 = wave.open(newAudioFile, 'w')
obj3.setnchannels(2)
obj3.setsampwidth(2)
obj3.setframerate(frame_rate)
obj3.writeframes(frames)
obj3.close()

# filter audio
# from pydub import *
from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_wav(audioFile)
print(audio)
# audio = audio[1000:2000] + audio[3000:4000]
# audio = audio.fade_in(5000)
print(audio.duration_seconds)
audio.export(mashAudioFile, format="wav")

# play audio segment
from playsound import playsound

input("Press Enter for Original")
playsound(audioFile)
input("Press Enter for New Audio")
playsound(newAudioFile)
input("Press Enter for Mash Audio")
playsound(mashAudioFile)
