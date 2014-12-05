#!/usr/bin/python3
#pythonpirate.py

import piratecode as CODE
import lighthouse as LIGHT

def ReadCodedMessage():
   while(1):
      codedmessage = input("Enter Coded Message:")
      print(codedmessage)
      if not all(x in ["-","*"," ","/"] for x in codedmessage):
         print("Use: -=Long flash *=Short flash")
      else:
         return codedmessage

def PlayCodedMessage(codedmessage):
   signal2Play=CODE.GetSignal(codedmessage)
   LIGHT.SendLighthouseSignal(signal2Play,signal2Play,signal2Play)

def PlayAgain(codedmessage):
   while(1):
      answer = input("Play again? Y/N:")
      if (answer.upper().startswith("Y")):
         PlayCodedMessage(codedmessage)
      elif (answer.upper() == "N"):
         return

def PlayMessage(message):
   codedmessage = CODE.GetCodedMessage(message)
   print(codedmessage)
   PlayCodedMessage(codedmessage)

def DecodeCodedMessage(codedmessage):
   message = CODE.GetMessage(codedmessage)
   return message

def main():
   codedmessage = ReadCodedMessage()
   PlayCodedMessage(codedmessage)
   PlayAgain(codedmessage)
   message = DecodeCodedMessage(codedmessage)
   if (message=="?"):
      print("Unknown code - try again!")
   else:
      print ("Message: ", message)


if __name__=="__main__":
   while(1):
      main()
