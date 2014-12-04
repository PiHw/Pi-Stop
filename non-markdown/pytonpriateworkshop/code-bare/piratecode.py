#!/usr/bin/python3
#piratecode.py

letter2code = {' ':'/',
               'N':'-*',
               'E':'*',
               'S':'***',
               'W':'*--'}
               

code2letter = dict((v,k) for k,v in letter2code.items())

ON,OFF=True,False
code2signal = {'*':[ON,OFF],
               '-':[ON,ON,ON,ON,OFF],
               ' ':[OFF],
               '/':[OFF]*3}

def GetLetter(code):
   try:
      return code2letter[code]
   except KeyError:
      print("Error: Code not found (",code,")")
      return "?"

def GetCode(letter):
   try:
      return letter2code[letter]
   except KeyError:
      print("Error: Letter not found (",letter,")")
      return "?"

def GetCodedMessage(message):
   codedmessage=""
   for letter in message.upper():
      codedmessage += (GetCode(letter))
      codedmessage += (" ")
   return codedmessage

def GetMessage(codedmessage):
   message=""
   codelist = codedmessage.split(" ")
      for code in codelist:
         message += (GetLetter(code))
      return message

def GetSignal(codedmessage):
   signal=[]
   for code in codedmessage:
      try:
         signal += code2signal[code]
      except KeyError:
         print("Error: Code not found")
         return []
   signal += code2signal[" "]
   return signal