#!/usr/bin/env python3
# from https://wiki.python.org/moin/UdpCommunication
# modified by RG Willhoft, 2020
# modified by Gabriel Lucena, 2021

import socket

UDP_IP = '192.168.15.37'
UDP_PORT = 5004

print( "UDP target IP:", UDP_IP )
print( "UDP target port:", UDP_PORT )
message = 'open'

# set up UDP socket
sock = socket.socket( socket.AF_INET,     # Internet
                      socket.SOCK_DGRAM ) # UDP


# send message
data = message.encode( "UTF-8" )
sock.sendto( data, ( UDP_IP, UDP_PORT ) )

# receive message
data, addr = sock.recvfrom( 1024 ) # 1024 byte buffer
message = data.decode( "UTF-8" )
print( "response:", message )
