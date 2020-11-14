import pyshorteners,pyjokes,pyttsx3,os,threading,socket,subprocess,pygame,time,sys
from googletrans import *
from gtts import gTTS
from covid import Covid
from threading import Thread
from playsound import playsound


def playAudiobackground ():
    playsound('s1.mp3')
    
def main():
    
    
    while True:
        
        print("\n\t\t\t\t*****WELCOME*******")
        print("\t\t\t| Press 1 For URL Shortner")
        print("\t\t\t| Press 2 For Jokes Generator")
        print("\t\t\t| Press 3 For Translator English to hindi ")
        print("\t\t\t| Press 4 Get Covid Updated Information For India")
        print("\t\t\t| Press 5 to ComputerName and It's IP Address")
        print("\t\t\t| Press 6 to Get WiFi Passwords")
        print("\t\t\t| Press 7 to Encrypt Message Into Mores Code")
        print("\t\t\t| Press 8 to Exit")
        
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
            elif choice==6:
                # now we will store the profiles data in "data" variable by 
                # running the 1st cmd command using subprocess.check_output
                data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

                # now we will store the profile by converting them to list
                profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

                # using for loop in python we are checking and printing the wifi 
                # passwords if they are available using the 2nd cmd command
                for i in profiles:
                    # running the 2nd cmd command to check passwords
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 
                                        'key=clear']).decode('utf-8').split('\n')
                    # storing passwords after converting them to list
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                    # printing the profiles(wifi name) with their passwords using 
                    # try and except method 
                    try:
                        print ("{:<30}|  {:<}".format(i, results[0]))
                    except IndexError:
                        print ("{:<30}|  {:<}".format(i, ""))
                               
                pass
            elif choice==7:
                #These are the dots and dashes or dits and dahs correspond to the alphabet

                CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
                        'D': '-..',    'E': '.',      'F': '..-.',
                        'G': '--.',    'H': '....',   'I': '..',
                        'J': '.---',   'K': '-.-',    'L': '.-..',
                        'M': '--',     'N': '-.',     'O': '---',
                        'P': '.--.',   'Q': '--.-',   'R': '.-.',
                        'S': '...',    'T': '-',      'U': '..-',
                        'V': '...-',   'W': '.--',    'X': '-..-',
                        'Y': '-.--',   'Z': '--..',
                        
                        '0': '-----',  '1': '.----',  '2': '..---',
                        '3': '...--',  '4': '....-',  '5': '.....',
                        '6': '-....',  '7': '--...',  '8': '---..',
                        '9': '----.' 
                        }
                        
                ONE_UNIT = 0.5
                THREE_UNITS = 3 * ONE_UNIT
                SEVEN_UNITS = 7 * ONE_UNIT
                PATH = 'morse_sound_files/' #The path of the audio file

                #The method Verifies that there shouldn't be any special characters
                def verify(string):
                    keys = CODE.keys()
                    for char in string:
                        if char.upper() not in keys and char != ' ':
                            sys.exit('Error the charcter ' + char + ' cannot be translated to Morse Code')

                def main():
                        
                    print('Welcome to Alphabet to Morse Code Translator v.01\n')
                    
                    msg = input('Enter Message: ')
                    verify(msg)
                    print
                    pygame.init()
                    fi=[]
                    for char in msg:
                        if char == ' ':
                            print (' '*7,
                            time.sleep(SEVEN_UNITS))
                        else:
                            print (CODE[char.upper()],
                            pygame.mixer.music.load(PATH + char.upper() + '_morse_code.ogg'))
                            pygame.mixer.music.play()
                            time.sleep(THREE_UNITS)
                            temp=CODE[char.upper()],pygame.mixer.music.load(PATH + char.upper() + '_morse_code.ogg')
                            fi.append(temp)


                    actualCode,noneList=zip(*fi) #unzipped the list here into two list to get the final Mores Code at the end 
                    
                    print("Your Moores Code:",''.join(actualCode))
                    print ('\n\nGoodbye!')
                    

                        
                if __name__ == "__main__":
                    main()
                
            
                pass
            elif choice ==8:
                quit()
               
            else:
                print("\ninvalid ! Try again")
        except Exception as e:
            print(e)
            print("invalid details ! Try again")

#Threading
t1=Thread(target=playAudiobackground)
t1.start()
t1=Thread(target=main)
t1.start()
