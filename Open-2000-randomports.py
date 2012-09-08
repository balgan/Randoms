from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor
import array
import resource
import string
import random
class SendContent(Protocol):
    def connectionMade(self):
        self.transport.write(self.factory.text)
        self.transport.loseConnection()

class SendContentFactory(Factory):
    protocol = SendContent
    def __init__(self, text=None):
        if text is None:
            text = """ROFL FUCK U!!!"""
        self.text = text

def openserver(PORT):
        try:
                reactor.listenTCP(PORT, SendContentFactory())
        except:
                print 'PORT IN USE:' + str(PORT)

def main():
        a=random.sample(range(1025,65000),1000)
        print "We decided to open ports" + str(a)
        for item in a:
                openserver(item)
        reactor.run()
main()

