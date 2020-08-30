import speech_recognition as sr


#r=sr.Recognizer()
#a=speech_recognition.AudioFile('1.wav')
#with a as source:
    #audio=r.record(source)
r=sr.Recognizer()
a=sr.AudioFile('1.wav')
with a as  source:
    audio=r.record(source)
text=r.recognize_google(audio)

file1=open(r"F:\java\Java Application\Magic\Game\2.txt","a")
file1.writelines(text)
file1.close()
