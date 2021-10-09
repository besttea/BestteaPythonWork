'''
Author:Zeng Ke 
Date: 2021-10-09 16:18:32
LastEditTime: 2021-10-10 07:52:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \0001\testsond.py
'''
import speech_recognition
import  pyttsx3

recognizer = speech_recognition.Recognizer()
print("Please start to speak:")
while True:
    try:
      with speech_recognition.Microphone(2) as mic:
          print("说话....")
          recognizer.adjust_for_ambient_noise(mic,duration=0.2)
          audio=recognizer.listen(mic)
          text=recognizer.recognize_google(audio,language="zh-CN")
          #text=text.lower()
          print(f"Recognized: {text}")
          
    except speech_recognition.UnknownValueError():
      recognizer =speech_recognition.Recognizer()
      print('I Could not....recognizing....')
      continue
