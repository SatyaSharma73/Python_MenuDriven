## Program Menu Consists :

 1. For URL Shortner
 2. For Jokes Generator
 3. For Translator Any Language 
 4. Covid Updated Information For India
 5. To get ComputerName and It's IP Address
 6. To Get WiFi Passwords
 7. To Encrypt Message Into Mores Code

## 1. URL SHORTNER
**URL shortening** is a technique on the World Wide Web n which a URL (**UNIFORM RESOURCE LOCATOR**) may be made substantially shorter and still direct to the required page.

***Library Required***

 1. pyshorteners
 
 A simple URL shortening API wrapper Python library.

 **Installing**

```
pip install pyshorteners
```
**Documentation**

[https://pyshorteners.readthedocs.io/en/latest/](https://pyshorteners.readthedocs.io/en/latest/)

## 2. Jokes Generator 
One line jokes for programmers (jokes as a service)

**Libraries Requires :**

 1. pyjokes
 2. pyttsx3

### Installation

1. Install the  ```pip install pyjokes  ``` module with pip.
2. Install the ```pip install pyttsx3```module with pip.

See the  [documentation](http://pyjok.es/install/)  for pyjokes installation instructions.
Documentation is available at  [https://pyjok.es/](https://pyjok.es/)
If you recieve errors such as  No module named win32com.client,  No module named win32, or  No module named win32api, you will need to additionally install  pypiwin32.

## Usage for pyttsx3:

```import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()```

## Changing Voice , Rate and Volume :

```import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()```
