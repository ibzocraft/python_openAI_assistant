#This program translates speech to text and text to speech using python speechrecognition with google audio 
# recon, and pyttsx3 for text to speech.

#Libraries
import speech_recognition
import pyttsx3
import pyaudio

#Recognizer
recognizer = speech_recognition.Recognizer()


#Text To Speech using pyttsx3
def SpeakText(text):
    tts_engine = pyttsx3.init()
    tts_engine.say(text)
    tts_engine.runAndWait()
    
    
    
#Infinite loop to analyse speech
while(1):
    
    #Exeption handling in case of Request or Unknown Error
    try:
        
        #Use microphone as input (audio source instance)
        with speech_recognition.Microphone(device_index=1) as mic:
            
            #Adjust the threshold according to the ambient noise level for a better listening
            print('Adjusting Threshold')
            recognizer.pause_threshold = 1      
            recognizer.adjust_for_ambient_noise(source=mic, duration=2)
            print('Done')
            
            #Listen to Speech
            print('Listening...')
            speech_audio = recognizer.listen(source=mic, timeout=30)
            print('Done')
            
            #Use google to recognize audio and translate it to Text
            print('Using Google Recognition')
            speech_text: str = recognizer.recognize_google_cloud(audio_data=speech_audio, credentials_json='')
            speech_text = speech_text.lower()
            print('Done')
            
            #Output text to terminal
            print("Did you say: ", speech_text)
            SpeakText(speech_text)
            
    except speech_recognition.RequestError as error:
        print(f'Could not request results, {error}')
    except speech_recognition.UnknownValueError:
        print(f'Unknown error occured')
    except speech_recognition.WaitTimeoutError:
        print('User Didnt Speak')
    except KeyboardInterrupt:
        print('Program Terminated')
        break
    
            