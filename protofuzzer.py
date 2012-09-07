#!/usr/bin/python
from scapy.all import *
from sys import *
import string
import random
import time

writer = PcapWriter("output.pcap", append=True)
protos_str = ["UDP","TCP","RIP","BOOTP","ARP","DHCP","DNS","ICMP","IP","LLC","MGCP","NTP","PPPoE","NetBIOS_DS","STP"]
if(str(argv[3]).upper() == "RANDOM"):
	print "Sending packet to ip " + str(argv[1]) + " to port " + argv[2] + " with protocol random"
else:
        print "Sending packet to ip " + str(argv[1]) + " to port " + argv[2] + " with protocol " + protos_str[int(argv[3])]


while(True):
		if(len(sys.argv) == 4):
			protos = [UDP(),TCP(),RIP(),BOOTP(),ARP(),DHCP(),DNS(),ICMP(),IP(),LLC(),MGCP(),NTP(),PPPoE(),NetBIOS_DS(),STP()]
                        chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
                        size = random.randrange(0, 1000, 2)
                        crashdata = ''.join(random.choice(chars) for x in range(size))
                        crashdata = crashdata.decode('hex')
			if(str(argv[2]).upper() == "RANDOM"):
                        	dportrand= random.randrange(0,65636)
	                        sportrand= random.randrange(0,65636)
			else:
				dportrand = int(argv[2])
                                sportrand = random.randrange(0,65636)
                        if(str(argv[3]).upper() == "RANDOM"):
                                packet=IP(dst=argv[1])/fuzz(protos[random.randrange(0,15)])
                                send(packet)
                                writer.write(packet)
				time.sleep(1)
			else:
	                        packet=IP(dst=argv[1])/fuzz(protos[int(argv[3])])
                	        send(packet)
                        	writer.write(packet)
				time.sleep(1)
		else:
                        print "ProtoFuzzer usage - protofuzzer.py <ip> <port> <protocol> - if no protocol is chosen default is TCP"
                        print "\nProtocols Supported - UDP (0),TCP (1),RIP (2),BOOTP (3),ARP (4),DHCP (5),DNS (6),ICMP (7),IP (8),LLC (9),MGCP (10),NTP (11),PPoE (12), random (random)"
			print "\nrandom will throw random protocol at random port"
                        print "\nExample usage: protofuzzer.py 192.168.1.69 22 1"
                        print "\nExample usage: protofuzzer.py 192.168.1.69 random random"
			sys.exit()