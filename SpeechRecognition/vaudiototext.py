import speech_recognition as sr
import moviepy.editor as mp
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

clip = mp.VideoFileClip(r"recording.mp4")
clip.audio.write_audiofile(r"converted.wav")

r = sr.Recognizer()
song = AudioSegment.from_wav("converted.wav")
chunks = split_on_silence(song, min_silence_len=500, silence_thresh= -16)
try:
    os.mkdir('audio_chunks')
except(FileExistsError):
    pass
os.chdir('audio_chunks')
i= 0
for chunk in chunks:
    chunk_silent = AudioSegment.silent(duration=10)
    audio_chunk = chunk_silent + chunk + chunk_silent
    audio_chunk.export("./chunk{0}.wav".format(i), bitrate='192k', format="wav")
    filename = 'chunk' + str(i) + '.wav'
    file = filename


audio = sr.AudioFile(file)

with audio as source:
    r.adjust_for_ambient_noise(source)
    audio_file = r.listen(source)

    result = r.recognize_ibm(audio_file,"B8VgHTnpv81ftOA_4CCOyxXSGVg7MwH2KJ_-iW5-5h_Y","Nightblood007@","en-US",False)
# exporting the result to text file

with open('recognized.txt',mode = 'w+') as file:
    file.write("Recognized Speech:")
    file.write("\n")
    file.write(result)
    print("ready!")

i+=1
os.chdir('..')