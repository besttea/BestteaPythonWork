'''
Author:Zeng Ke 
Date: 2021-10-09 16:18:32
LastEditTime: 2021-10-10 09:36:04
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
          print(mic.device_index)
          recognizer.adjust_for_ambient_noise(mic,duration=0.2)
          audio=recognizer.listen(mic)
          text=recognizer.recognize_google(audio,language="zh-CN")
          #text=text.lower()
          print(f"Recognized: {text}")
          if text =="停止":
            print("拜拜了，您！")
            break
          
    except speech_recognition.UnknownValueError():
      recognizer =speech_recognition.Recognizer()
      print('I Could not....recognizing....')
      continue
