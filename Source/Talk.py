from chatterbot import ChatBot
import logging
import speech_recognition as sr
from subprocess import Popen, PIPE, STDOUT
import os

r = sr.Recognizer()
m = sr.Microphone()
# Comment next line and start daemon seperately for debug
os.system('\\nohup ruby daemon.rb &')
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
except KeyboardInterrupt:
    pass

# Create a new instance of a ChatBot
bot = ChatBot("Terminal",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="database.db"
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        print("Sprechen Sie.")
        with m as source: audio = r.listen(source)
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            print("Ich habe verstanden: {}".format(value))
            verstehe = format(value)
            bot_output = bot.get_response(verstehe)
            towatir = open("pythonruby.xml", "w")
            line = towatir.write(bot_output)
            towatir.close()
            #os.system('\\nohup ruby goowatir.rb \"' + bot_output + '\" &')

            #For animation control with Processing host. Rarely needing this but .pde must be somewhere!
            #processing = open("data/talk_bool.xml", "w")
            #line = processing.write("1")
            #processing.close()

        except sr.UnknownValueError:
            print("Ich kann nichts hören.")
            #processing = open("data/talk_bool.xml", "w")
            #line = processing.write("0")
            #processing.close()
        except sr.RequestError as e:
            print("Ohje. Ich muss schlafen gehen. ; {0}".format(e))

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
