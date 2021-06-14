import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("GOod Morning!!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("Hello Tejas! Please tell me how may I help you ?")    
    
    
def takeCommand():
    # it takes microphone input from user & return string output   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("Say that again please...\n")
        return "None"
    return query
    
    

# main funtion for clean purpose
if __name__ == '__main__':
    wishMe()

    while True:
        query = takeCommand().lower()
        # logic for executing tasks :
        if 'custom search' in query:
            print("Custom Search Action enabled !!")
            speak("Please specify custom search")
            customSearchQuery = takeCommand().lower()
            webbrowser.open(customSearchQuery)
            
        elif 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            print(results)
            speak(results)
        
        # program exit
        elif 'system exit' in query:
            print('Exiting...')
            speak('Exiting...')
            speak('Thanks for using me !!.....')
            # break
            exit()
            
        # restart & shutdown
        elif 'system shutdown' in query or 'system shut down' in query:
            print('Shutting down...')
            speak('Shutting down...')
            speak('See You Next time !!.....')
            os.system("shutdown /s")
        elif 'system restart' in query:
            print('Restarting your PC...')
            speak('Restarting your PC...')
            speak('See You Next time !!.....')
            os.system("shutdown /r")
            
        
        elif 'open youtube' in query:
            print("Opening YouTube...")
            speak("Opening YouTube...")
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.open("www.google.com")

            
        elif 'brave' in query:
            disha = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            print("Opening Brave...")
            speak("Opening Brave...")
            os.startfile(disha)
            
            
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir, the time is {strtime}")
         
        # specific applications   
        elif 'open code' in query:
            code_path = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("Opening vscode...")
            speak("Opening vscode...")
            os.startfile(code_path)
            
        elif 'college book' in query:
            a = "D:\\Books"
            print("Opening Books folder...")
            speak("Opening Books folder...")
            os.startfile(a)
            
    
            
            
            
            
    
    
        
        
    