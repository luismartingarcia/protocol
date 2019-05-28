################################################################################
#                    ____            _                  _                      #
#                   |  _ \ _ __ ___ | |_ ___   ___ ___ | |                     #
#                   | |_) | '__/ _ \| __/ _ \ / __/ _ \| |                     #
#                   |  __/| | | (_) | || (_) | (_| (_) | |                     #
#                   |_|   |_|  \___/ \__\___/ \___\___/|_|                     #
#                                                                              #
#           == A Simple ASCII Header Generator for Network Protocols ==        #
#                                                                              #
################################################################################
#                                                                              #
#  Written by:                                                                 #
#                                                                              #
#     Luis MartinGarcia.                                                       #
#       -> E-Mail: luis.mgarc@gmail.com                                        #
#       -> WWWW:   http://www.luismg.com                                       #
#       -> GitHub: https://github.com/luismartingarcia                         #
#                                                                              #
################################################################################
#                                                                              #
#  This file is part of Protocol.                                              #
#                                                                              #
#  Copyright (C) 2014 Luis MartinGarcia (luis.mgarc@gmail.com)                 #
#                                                                              #
#  This program is free software: you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation, either version 3 of the License, or           #
#  (at your option) any later version.                                         #
#                                                                              #
#  This program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                              #
#  Please check file LICENSE.txt for the complete version of the license,      #
#  as this disclaimer does not contain the full information. Also, note        #
#  that although Protocol is licensed under the GNU GPL v3 license, it may     #
#  be possible to obtain copies of it under different, less restrictive,       #
#  alternative licenses. Requests will be studied on a case by case basis.     #
#  If you wish to obtain Protocol under a different license, please contact    #
#  the email address mentioned above.                                          #
#                                                                              #
################################################################################
#                                                                              #
# Description:                                                                 #
#                                                                              #
#  This file contains popular protocol specs.                                  #
#                                                                              #
################################################################################

#
#      0                   1                   2                   3                   4
#      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                      Destination Address                                      |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                         Source Address                                        |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |           EtherType           |                                                               |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                                               +
#     |                                                                                               |
#     +                                            Payload                                            +
#     |                                                                                               |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
ethernet="Destination Address:48,Source Address:48,EtherType:16,Payload:128?bits=48"


#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                      Destination Address                                      |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                         Source Address                                        |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |         TPID (0x8100)         | PCP |D|        VLAN ID        |           EtherType           |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                                                                               |
#     +                                            Payload                                            +
#     |                                                                                               |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
dot1q="Destination Address:48,Source Address:48,TPID (0x8100):16,PCP:3,D:1,\
VLAN ID:12,EtherType:16,Payload:96?bits=48"


#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |          Source Port          |       Destination Port        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                        Sequence Number                        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                    Acknowledgment Number                      |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    | Offset|  Res. |     Flags     |             Window            |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |           Checksum            |         Urgent Pointer        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                    Options                    |    Padding    |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                             data                              |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
tcp="Source Port:16,Destination Port:16,Sequence Number:32,\
Acknowledgment Number:32,Offset:4,Res.:4,Flags:8,Window:16,Checksum:16,\
Urgent Pointer:16,Options:24,Padding:8"


#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |          Source Port          |       Destination Port        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |            Length             |            Checksum           |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
udp="Source Port:16,Destination Port:16,Length:16,Checksum:16"


#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |Version|  IHL  |Type of Service|          Total Length         |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |         Identification        |Flags|      Fragment Offset    |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |  Time to Live |    Protocol   |         Header Checksum       |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                       Source Address                          |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                    Destination Address                        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                    Options                    |    Padding    |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
ip="Version:4,IHL:4,Type of Service:8,Total Length:16,Identification:16,\
Flags:3,Fragment Offset:13,Time to Live:8,Protocol:8,Header Checksum:16,\
Source Address:32,Destination Address:32,Options:24,Padding:8"

#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |Version| Traffic Class |           Flow Label                  |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |         Payload Length        |  Next Header  |   Hop Limit   |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                                                               |
#    +                                                               +
#    |                                                               |
#    +                         Source Address                        +
#    |                                                               |
#    +                                                               +
#    |                                                               |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                                                               |
#    +                                                               +
#    |                                                               |
#    +                      Destination Address                      +
#    |                                                               |
#    +                                                               +
#    |                                                               |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
ipv6="Version:4,Traffic Class:8,Flow Label:20,Payload Length:16,Next Header:8,\
Hop Limit:8, Source Address:128, Destination Address:128"


# ICMPv4 Generic Header
#
#      0                   1                   2                   3
#      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |      Type     |      Code     |            Checksum           |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                                               |
#     +                          Message Body                         +
#     |                                                               |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
icmp="Type:8,Code:8,Checksum:16,Message Body:64"


# ICMPv4 Destination Unreachable Message
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Type      |     Code      |          Checksum             |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                             unused                            |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |      Internet Header + 64 bits of Original Data Datagram      |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
icmp_destination="Type:8,Code:8,Checksum:16,Unused:32,Internet Header + 64 bits\
 of Original Data Datagram:64"


# ICMPv4 Time Exceeded Message
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Type      |     Code      |          Checksum             |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                             unused                            |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |      Internet Header + 64 bits of Original Data Datagram      |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
icmp_time="Type:8,Code:8,Checksum:16,Unused:32,Internet Header + 64 bits of\
 Original Data Datagram:64"


# ICMPv4 Parameter Problem Message
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Type      |     Code      |          Checksum             |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |    Pointer    |                   unused                      |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |      Internet Header + 64 bits of Original Data Datagram      |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
icmp_parameter="Type:8,Code:8,Checksum:16,Pointer:8,Unused:24,Internet Header\
 + 64 bits of Original Data Datagram:64"


# ICMPv4 Source Quench Message
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Type      |     Code      |          Checksum             |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                             unused                            |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |      Internet Header + 64 bits of Original Data Datagram      |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
icmp_source="Type:8,Code:8,Checksum:16,Unused:32,Internet Header + 64 bits of\
 Original Data Datagram:64"


# ICMPv4 Redirect Message
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Type      |     Code      |          Checksum             |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |                 Gateway Internet Address                      |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |      Internet Header + 64 bits of Original Data Datagram      |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
icmp_redirect="Type:8,Code:8,Checksum:16,Gateway Internet Address:32,Internet\
 Header + 64 bits of Original Data Datagram:64"


# ICMPv4 Echo or Echo Reply Message
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Type      |     Code      |          Checksum             |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |           Identifier          |        Sequence Number        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Data ...
#    +-+-+-+-+-
icmp_echo="Type:8,Code:8,Checksum:16,Identifier:16,Sequence Number:16,Data:64"


# ICMPv4 Timestamp or Timestamp Reply Message
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Type      |      Code     |          Checksum             |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |           Identifier          |        Sequence Number        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Originate Timestamp                                       |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Receive Timestamp                                         |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Transmit Timestamp                                        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
icmp_timestamp="Type:8,Code:8,Checksum:16,Identifier:16,Sequence Number:16,\
Originate Timestamp:32,Receive Timestamp:32,Transmit Timestamp:32"


# ICMPv4 Information Request or Information Reply Message
#
#     0                   1                   2                   3
#     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |     Type      |      Code     |          Checksum             |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#    |           Identifier          |        Sequence Number        |
#    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
icmp_information="Type:8,Code:8,Checksum:16,Identifier:16,Sequence Number:16"


# ICMPv6 General Format
#
#        0                   1                   2                   3
#        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |     Type      |     Code      |          Checksum             |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                                                               |
#       +                         Message Body                          +
#       |                                                               |
icmpv6="Type:8,Code:8,Checksum:16,Message Body:64"


# ICMPv6 Destination Unreachable Message
#
#        0                   1                   2                   3
#        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |     Type      |     Code      |          Checksum             |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                             Unused                            |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |  Invoking packet data (without exceeding minimum IPv6 MTU)      |
#       +                as possible without the ICMPv6 packet          +
#       |                exceeding the minimum IPv6 MTU [IPv6]          |
icmpv6_destination="Type:8,Code:8,Checksum:16,Unused:32,Invoking packet data\
 (without exceeding minimum IPv6 MTU):64"


# ICMPv6 Packet Too Big Message
#
#        0                   1                   2                   3
#        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |     Type      |     Code      |          Checksum             |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                             MTU                               |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                    As much of invoking packet                 |
#       +               as possible without the ICMPv6 packet           +
#       |               exceeding the minimum IPv6 MTU [IPv6]           |
icmpv6_big="Type:8,Code:8,Checksum:16,MTU:32,Invoking packet data (without\
 exceeding minimum IPv6 MTU):64"


# ICMPv6 Time Exceeded Message
#
#        0                   1                   2                   3
#        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |     Type      |     Code      |          Checksum             |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                             Unused                            |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                    As much of invoking packet                 |
#       +               as possible without the ICMPv6 packet           +
#       |               exceeding the minimum IPv6 MTU [IPv6]           |
icmpv6_time="Type:8,Code:8,Checksum:16,Unused:32,Invoking packet data (without\
 exceeding minimum IPv6 MTU):64"


# ICMPv6 Parameter Problem Message
#
#        0                   1                   2                   3
#        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |     Type      |     Code      |          Checksum             |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                            Pointer                            |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                    As much of invoking packet                 |
#       +               as possible without the ICMPv6 packet           +
#       |               exceeding the minimum IPv6 MTU [IPv6]           |
icmpv6_parameter="Type:8,Code:8,Checksum:16,Pointer:32,Invoking packet data\
 (without exceeding minimum IPv6 MTU):64"


# ICMPv6 Echo Request and Reply Message
#
#        0                   1                   2                   3
#        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |     Type      |     Code      |          Checksum             |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |           Identifier          |        Sequence Number        |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |     Data ...
#       +-+-+-+-+-
icmpv6_echo="Type:8,Code:8,Checksum:16,Identifier:16,Sequence Number:16,Data:64"


# ICMPv6 Router Solicitation Message Format
#
#       0                   1                   2                   3
#       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |     Type      |     Code      |          Checksum             |
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |                            Reserved                           |
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |   Options ...
#      +-+-+-+-+-+-+-+-+-+-+-+-
icmpv6_rsol="Type:8,Code:8,Checksum:16,Reserved:32,Options:64"


# ICMPv6 Router Advertisement Message Format
#
#       0                   1                   2                   3
#       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |     Type      |     Code      |          Checksum             |
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      | Cur Hop Limit |M|O|  Reserved |       Router Lifetime         |
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |                         Reachable Time                        |
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |                          Retrans Timer                        |
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |   Options ...
#      +-+-+-+-+-+-+-+-+-+-+-+-
icmpv6_radv="Type:8,Code:8,Checksum:16,Cur Hop Limit:8,M:1,O:1,Reserved:6,\
Router Lifetime:16,Reachable Time:32,Retransmission Timer:32,Options:64"


# ICMPv6 Neighbor Solicitation Message Format
#
#       0                   1                   2                   3
#       0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |     Type      |     Code      |          Checksum             |
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |                           Reserved                            |
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |                                                               |
#      +                                                               +
#      |                                                               |
#      +                       Target Address                          +
#      |                                                               |
#      +                                                               +
#      |                                                               |
#      +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#      |   Options ...
#      +-+-+-+-+-+-+-+-+-+-+-+-
icmpv6_nsol="Type:8,Code:8,Checksum:16,Reserved:32,Target Address:128,\
Options:64"


# ICMPv6 Neighbor Advertisement Message Format
#
#        0                   1                   2                   3
#        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |     Type      |     Code      |          Checksum             |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |R|S|O|                     Reserved                            |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                                                               |
#       +                                                               +
#       |                                                               |
#       +                       Target Address                          +
#       |                                                               |
#       +                                                               +
#       |                                                               |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |   Options ...
#       +-+-+-+-+-+-+-+-+-+-+-+-
icmpv6_nadv="Type:8,Code:8,Checksum:16,R:1,S:1,O:1,Reserved:29,Target\
 Address:128,Options:64"


# ICMPv6 Redirect Message Format
#
#        0                   1                   2                   3
#        0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |     Type      |     Code      |          Checksum             |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                           Reserved                            |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                                                               |
#       +                                                               +
#       |                                                               |
#       +                       Target Address                          +
#       |                                                               |
#       +                                                               +
#       |                                                               |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |                                                               |
#       +                                                               +
#       |                                                               |
#       +                     Destination Address                       +
#       |                                                               |
#       +                                                               +
#       |                                                               |
#       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#       |   Options ...
#       +-+-+-+-+-+-+-+-+-+-+-+-
icmpv6_redirect="Type:8,Code:8,Checksum:16,Reserved:32,Target Address:128,\
Destination Address:128,Options:64"

dhcp = "Opcode:8,Hardware Type: 8,HW Addr Len:8,Hop Count:8,Transaction ID:32,Number of Seconds:16,Flags:16,Client IP Addr:32,Your IP Addr: 32,Server IP Addr:32,Gateway IP Addr:32,Client Hardware Addr:128,Server Host Name:512,Boot Filename:1024"

modbus_tcp="Transaction ID:16,Protocol ID:16,Length:16,Address:8,Function Code:8,Data:64"

profinet_rt="Frame ID:16,User Data:80,Cycle Counter:16,Data Status:8,Transfer Status:8"

dnp3="Start:16,Length:8,Control:8,Destination Address:16,Source Address:16,CRC:16,User Data 1:128,CRC 1:16,User Data 2:112,CRC 2:16"

tsap="Type:8,Slot:5,Rack:3?bits=16"

cotp_cr="Length:8,PDU Type:8, Destination Reference:16, Source Reference:16,Class/Options:8,Param. Code:8,Param. Length:8,Param.:88"

cotp_dt="Length:8,PDU Type:8,Num. & LDU:8?bits=24"

cotp_dr="Length:8,PDU Type:8, Destination Reference:16, Source Reference:16,Cause:8"

s7_header="Protocol ID:8,ROSCTR:8,Reserved:16,Request ID:16,Parameter Length:16,Data Length:16,Error Code (only ROSCTR 3):16,Function Code:8,Item Count:8?bits=16"

s7_item="Var Type:8,Var Length:8,Syntax ID:8,Transport Size:8,Length:16,DB Number:16,Area:8,Address:24"

s7_data="Return Code:8,Transport Size:8,Data Length:16"

#      0                   1
#      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
#     *-------------------------------*
#     | Field4| Field4|     Field8    |
#     *-------------------------------*
#     |            Field16            |
#     *-------------------------------*
#     |                               |
#     *            Field32            *
#     |                               |
#     *-------------------------------*
#     |                               |
#     *                               *
#     |                               |
#     *            Field64            *
#     |                               |
#     *                               *
#     |                               |
#     *-------------------------------*
example="Field4:4,Field4:4,Field8:8,Field16:16,Field32:32,Field64:64?bits=16,\
numbers=y,startchar=*,endchar=*,evenchar=-,oddchar=-,sepchar=|"


#      0                   1                   2                   3
#      0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |F|Field_4|   Field_7   |      Field_10     |      Field_13     |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |     |            Field_16           |         Field_19        |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |           |                  Field_22                 |       |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                 Field_25                |                     |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |             Field_28            |                             |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |            Field_31           |                               |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |              Field_34             |                           |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+         +-+-+-+-+-+-+-+-+-+
#     |                   Field_37                  |                 |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+               +-+
#     |                           Field_40                          | |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +
#     |                            Field_43                           |
#     +                   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                   |                                           |
#     +-+-+-+-+-+-+-+-+-+-+                           +-+-+-+-+-+-+-+-+
#     |                    Field_46                   |               |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+               +
#     |                            Field_49                           |
#     +                 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                 |                                             |
#     +-+-+-+-+-+-+-+-+-+                                       +-+-+-+
#     |                         Field_52                        |     |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+     +
#     |                            Field_55                           |
#     +                                       +-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                       |                       |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                       +
#     |                            Field_58                           |
#     +                           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                           |                                   |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                   +
#     |                            Field_61                           |
#     +                     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                     |                                         |
#     +-+-+-+-+-+-+-+-+-+-+-+                                         +
#     |                            Field_64                           |
#     +                     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                     |                                         |
#     +-+-+-+-+-+-+-+-+-+-+-+                                         +
#     |                            Field_67                           |
#     +                           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                           |                                   |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                   +
#     |                            Field_70                           |
#     +                                       +-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                       |                       |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                       +
#     |                            Field_73                           |
#     +                                                         +-+-+-+
#     |                                                         |     |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+     +
#     |                                                               |
#     +                                                               +
#     |                            Field_76                           |
#     +                 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                 |                                             |
#     +-+-+-+-+-+-+-+-+-+                                             +
#     |                            Field_79                           |
#     +                                               +-+-+-+-+-+-+-+-+
#     |                                               |               |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+               +
#     |                                                               |
#     +                                                               +
#     |                            Field_82                           |
#     +                   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                   |                                           |
#     +-+-+-+-+-+-+-+-+-+-+                                           +
#     |                            Field_85                           |
#     +                                                             +-+
#     |                                                             | |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +
#     |                                                               |
#     +                                                               +
#     |                            Field_88                           |
#     +                                             +-+-+-+-+-+-+-+-+-+
#     |                                             |                 |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                 +
#     |                                                               |
#     +                                                               +
#     |                            Field_91                           |
#     +                                   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                   |                           |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                           +
#     |                                                               |
#     +                                                               +
#     |                            Field_94                           |
#     +                               +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                               |                               |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                               +
#     |                                                               |
#     +                                                               +
#     |                            Field_97                           |
#     +                                 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                 |                             |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                             +
#     |                                                               |
#     +                                                               +
#     |                           Field_100                           |
#     +                                         +-+-+-+-+-+-+-+-+-+-+-+
#     |                                         |                     |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                     +
#     |                                                               |
#     +                                                               +
#     |                           Field_103                           |
#     +                                                       +-+-+-+-+
#     |                                                       |       |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+       +
#     |                                                               |
#     +                                                               +
#     |                                                               |
#     +                                                               +
#     |                           Field_106                           |
#     +           +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |           |                                                   |
#     +-+-+-+-+-+-+                                                   +
#     |                                                               |
#     +                                                               +
#     |                           Field_109                           |
#     +                                     +-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                                     |                         |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                         +
#     |                                                               |
#     +                                                               +
#     |                                                               |
#     +                                                               +
#     |                           Field_112                           |
#     +     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |     |                                                         |
#     +-+-+-+                                                         +
#     |                                                               |
#     +                                                               +
#     |                           Field_115                           |
#     +                                           +-+-+-+-+-+-+-+-+-+-+
#     |                                           |                   |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                   +
#     |                                                               |
#     +                                                               +
#     |                                                               |
#     +                                                               +
#     |                           Field_118                           |
#     +                       +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |                       |                                       |
#     +-+-+-+-+-+-+-+-+-+-+-+-+                                       +
#     |                                                               |
#     +                                                               +
#     |                                                               |
#     +                                                               +
#     |                           Field_121                           |
#     +         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     |         |                                                     |
#     +-+-+-+-+-+                                                     +
#     |                                                               |
#     +                                                               +
#     |                                                               |
#     +                                                               +
#     |                           Field_124                           |
#     + +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#     | |                                                             |
#     +-+                                                             +
#     |                                                               |
#     +                                                               +
#     |                           Field_127                           |
#     +                                                               +
#     |                                                               |
#     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
test="Field_1:1,Field_4:4,Field_7:7,Field_10:10,Field_13:13,Field_16:16,\
Field_19:19,Field_22:22,Field_25:25,Field_28:28,Field_31:31,Field_34:34,\
Field_37:37,Field_40:40,Field_43:43,Field_46:46,Field_49:49,Field_52:52,\
Field_55:55,Field_58:58,Field_61:61,Field_64:64,Field_67:67,Field_70:70,\
Field_73:73,Field_76:76,Field_79:79,Field_82:82,Field_85:85,Field_88:88,\
Field_91:91,Field_94:94,Field_97:97,Field_100:100,Field_103:103,Field_106:106,\
Field_109:109,Field_112:112,Field_115:115,Field_118:118,Field_121:121,\
Field_124:124,Field_127:127"


# Dictionary of specs
protocols={"ethernet":ethernet,
           "8021q":dot1q,
           "dot1q":dot1q,
           "tcp":tcp,
           "udp":udp,
           "ip":ip,
           "ipv6":ipv6,
           "icmp":icmp,
           "icmp-destination":icmp_destination,
           "icmp-time":icmp_time,
           "icmp-parameter":icmp_parameter,
           "icmp-source":icmp_source,
           "icmp-redirect":icmp_redirect,
           "icmp-echo":icmp_echo,
           "icmp-timestamp":icmp_timestamp,
           "icmp-information":icmp_information,
           "icmpv6":icmpv6,
           "icmpv6-destination":icmpv6_destination,
           "icmpv6-big":icmpv6_big,
           "icmpv6-time":icmpv6_time,
           "icmpv6-parameter":icmpv6_parameter,
           "icmpv6-echo":icmpv6_echo,
           "icmpv6-rsol":icmpv6_rsol,
           "icmpv6-radv":icmpv6_radv,
           "icmpv6-nsol":icmpv6_nsol,
           "icmpv6-nadv":icmpv6_nadv,
           "icmpv6-redirect":icmpv6_redirect,
           "dhcp": dhcp,
           "modbus_tcp":modbus_tcp,
           "profinet_rt":profinet_rt,
           "tsap":tsap,
           "dnp3":dnp3,
           "s7_header":s7_header,
           "s7_item":s7_item,
           "s7_data":s7_data,
           "cotp_cr":cotp_cr,
           "cotp_dt":cotp_dt,
           "cotp_dr":cotp_dr,
           "example":example,
           "test":test
           }

