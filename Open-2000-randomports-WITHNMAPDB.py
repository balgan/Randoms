from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import array
import resource
import string
import random
import os
filename = "NMAPFINALNOSPACE"
file = open(filename,'r')
file_size = os.stat(filename)[6]
class SendContent(Protocol):
    def connectionMade(self):
        self.transport.write(self.factory.text)
        self.transport.loseConnection()

class SendContentFactory(Factory):
    protocol = SendContent
    def __init__(self, text=None):
        if text is None:
            file.seek((file.tell()+random.randint(0,file_size-1))%file_size)
            file.readline()
            text = file.readline()
            print text
        self.text = text

def openserver(PORT):
        try:
                reactor.listenTCP(PORT, SendContentFactory())
                print 'PORT AVAILABLE' + str(PORT)
        except:
                print 'PORT IN USE:' + str(PORT)

def main():
        a=random.sample(range(1025,65000),1000)
        print "We decided to open ports" + str(a)
        for item in a:
                openserver(item)
        reactor.run()
main()
