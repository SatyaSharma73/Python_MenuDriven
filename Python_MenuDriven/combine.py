import pyshorteners
import pyjokes
import pyttsx3
from googletrans import *
from gtts import gTTS
import os
from covid import Covid
import socket 

def main():
    while True:
        
        print("\n\t\t\t\t*****WELCOME*******")
        print("\t\t\t| Press 1 For URL Shortner")
        print("\t\t\t| Press 2 For Jokes Generator")
        print("\t\t\t| Press 3 For Translator English to hindi ")
        print("\t\t\t| Press 4 Get Covid Updated Information For India")
        print("\t\t\t| Press 5 to ComputerName and It's IP Address")
        print("\t\t\t| Press 6 to Exit")
        
        print()
        try:
            choice=int(input())
            if(choice==1):
                url = input("Enter your url")
                s = pyshorteners.Shortener().tinyurl.short(url)
                print("Your shorted is -->", s)
                
                pass
            elif choice==2:
                joke=pyjokes.get_joke()
                print(joke)

                engine=pyttsx3.init()
                """ RATE"""
                rate = engine.getProperty('rate')   # getting details of current speaking rate
                engine.setProperty('rate', 200)     # setting up new voice rate
                """VOLUME"""
                volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
                engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
                """VOICE"""
                voices = engine.getProperty('voices')       #getting details of current voice
                #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
                engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
                print("Narrating the joke ")

                engine.say(joke)
                engine.runAndWait()
                
                pass
            elif choice==3:
                #text = '''The computer was born to solve problems that did not exist before'''
                print("Langauges : ")
                print(''''af'--'Afrikaans', 'sq'--'Albanian','ar'--'Arabic','hy'--'Armenian',
                         'bn'--'Bengali','ca'--'Catalan','zh'--'Chinese','zh-cn'--'Chinese (Mandarin/China)',
                         'zh-tw'--'Chinese (Mandarin/Taiwan)','zh-yue'--'Chinese (Cantonese)','hr'--'Croatian',
                         'cs'--'Czech','da'--'Danish','nl'--'Dutch','en'--'English','en-au'--'English (Australia)',
                         'en-uk'--'English (United Kingdom)','en-us'--'English (United States)','fi'--'Finnish',
                         'fr'--'French','de'--'German','el'--'Greek','hi'--'Hindi','hu'--'Hungarian','is'--'Icelandic',
                         'id'--'Indonesian','it'--'Italian','ja'--'Japanese','ko'--'Korean','la'--'Latin','lv'--'Latvian',
                         'mk'--'Macedonian','no'--'Norwegian','pl'--'Polish','pt'--'Portuguese',
                         'pt-br'--'Portuguese (Brazil)','ro'--'Romanian','ru'--'Russian','sr'--'Serbian',
                         'sk'--'Slovak','es'--'Spanish','es-es'--'Spanish (Spain)','es-us'--'Spanish (United States)',
                         'sw'--'Swahili','sv'--'Swedish','ta'--'Tamil','th'--'Thai',
                         'tr'--'Turkish','vi'--'Vietnamese','cy'--'Welsh''')
                lang=input("Enter the langauge You want to convert into ")
                text=input("Enter Word/phrase")
                translator = Translator()            
                temp= translator.detect(text)
                print('-----------------------------------------------------------------------')
                print('The Text is :')
                print(text,"\n")
                translated = translator.translate(text,dest=lang) #Change en into any langauge you want from below list

# 'af':'Afrikaans', 'sq':'Albanian','ar':'Arabic','hy':'Armenian','bn':'Bengali','ca':'Catalan','zh':'Chinese','zh-cn':'Chinese (Mandarin/China)',
# 'zh-tw':'Chinese (Mandarin/Taiwan)','zh-yue':'Chinese (Cantonese)','hr':'Croatian','cs':'Czech','da':'Danish','nl':'Dutch','en':'English','en-au':'English (Australia)',
# 'en-uk':'English (United Kingdom)','en-us':'English (United States)','fi':'Finnish','fr':'French','de':'German','el':'Greek','hi':'Hindi','hu':'Hungarian','is':'Icelandic',
# 'id':'Indonesian','it':'Italian','ja':'Japanese','ko':'Korean','la':'Latin','lv':'Latvian','mk':'Macedonian','no':'Norwegian','pl':'Polish','pt':'Portuguese',
# 'pt-br':'Portuguese (Brazil)','ro':'Romanian','ru':'Russian','sr':'Serbian','sk':'Slovak','es':'Spanish','es-es':'Spanish (Spain)','es-us':'Spanish (United States)',
# 'sw':'Swahili','sv':'Swedish','ta':'Tamil','th':'Thai','tr':'Turkish','vi':'Vietnamese','cy':'Welsh'

                print("SOURCE Langauge : ",translated.src)
                print("DESTINATION Langauge : ",translated.dest,"\n")

                print("Translated :")
                print(translated.text)
                print("please wait...processing")
                TTS = gTTS(text=translated.text, lang='en-in') #lang changes the accent

#Accents -

#en-au (Australia)
# en-gb (United Kingdom)
# en-in (India)
# en-us (United States)

                # Save to mp3 in current dir.
                TTS.save("voice.mp3")

                # Plays the mp3 using the default app on your system
                # that is linked to mp3s.
                os.system("start voice.mp3")
                
                pass
            elif choice == 4:
                # initializing
                covid = Covid()
                # printing data for the world
                print("Total active cases in world:", covid.get_total_active_cases())
                print("Total recovered cases in world:", covid.get_total_recovered())
                print("Total deaths in world:", covid.get_total_deaths())
                # getting data according to country name
                # data will be stored as a dictionary
                
                cases = covid.get_status_by_country_name("INDIA") 
                # printing country's data using for loop
                for x in cases:
                    print(x, ":", cases[x])
               
                pass
            elif choice==5:                
                # getting machine name
                hostname = socket.gethostname() 
                # getting IP Address
                IPAddr = socket.gethostbyname(hostname) 
                # printing hostname
                print("Your Computer Name is:" + hostname) 
                # printing IP Address
                print("Your Computer IP Address is:" + IPAddr)
                pass 
            elif choice == 6:
                break
            else:
                print("\ninvalid ! Try again")
        except Exception as e:
            print(e)
            print("invalid details ! Try again")

if __name__=="__main__":
    main()