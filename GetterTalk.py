#!/usr/bin/python -tt
# Have a conversation with a PandaBot AI
# Author A.Roots

import urllib, urllib2
import sys
from xml.dom import minidom
from xml.sax.saxutils import unescape

def main():
  
  human_input = raw_input('You: ')
  if human_input == 'exit':
    sys.exit(0)
  
  base_url = 'http://www.pandorabots.com/pandora/talk-xml'
  data = urllib.urlencode([('botid', 'ebbf27804e3458c5'), ('input', human_input)])
  
  # Submit POST data and download response XML
  req = urllib2.Request(base_url)
  fd = urllib2.urlopen(req, data)
  
  # Take Bot's response out of XML
  xmlFile = fd.read()
  dom = minidom.parseString(xmlFile)
  objektid = dom.getElementsByTagName('that')
  bot_response = objektid[0].toxml()
  bot_response = bot_response[6:]
  bot_response = bot_response[:-7]
  # Some nasty unescaping
  bot_response = unescape(bot_response, {"&apos;": "'", "&quot;": '"'})
  
  print 'Getter:',str(bot_response)
  
  # Repeat until terminated
  while 1:
    main()

if __name__ == '__main__':
  print 'Hi. You can now talk to Getter. Type "exit" when done.'
  main()