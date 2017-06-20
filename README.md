## - Talk -
#### Hacky engine to talk with your computer  

You must have read all the contracts you ever made with Google before using this software.  

Pipeline for: Speech to text input -> Chatbot -> Text to speech response using Python SpeechRecognition, Chatterbot and Watir Webdriver  

Talk to your command line and it will answer you something machine-learned with a nice voice.  
Gets smarter the more it communicates.  

Modules:  
- Python speech_recognition awaiting your voice. It works with Natural Language Toolkit. For this I hacked together some language data I found online for German French and English.  
- Python Chatterbot, a machine learning engine that learns how to speak by communicating.  
- A Ruby daemon based on Watir-Webdriver to use Google Translate as voice-output. This is gray-zone. Don't use it.  

Communication between Ruby and Python happens over an .XML file. XD  

How to install:  
Try and launch the binary. If it works right out of the box you must be god.  
Another approach is to place ntlk-data in one of the following locations:  
```
'~/'
'/usr/share/'
'/usr/local/share/'
'/usr/lib/'
'/usr/local/lib/'
```  
... and go with the source.  
Install the sources python dependencies in source folder with
```
pip install -r requirements.txt
```
I got it running on a Raspbian Jessie. Only part that did not work was speech output via Google, because the Firefox-Geckodriver doesn't work on ARM. So close!  
