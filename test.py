#!/usr/bin/python
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
#  Unit tests for the "protocol" tool                                          #
#                                                                              #
################################################################################

# STANDARD LIBRARY IMPORTS
import imp
import unittest

# IMPORT PROTOCOL (need to use the imp library since "protocol" does not 
# have a .py extension
protocol = imp.load_source("protocol", "protocol")

# List of test cases. It contains tuples of the form (protocol_spec, expected_output)
validcases=[
           
("Field_32:32", 
""" 0                   1                   2                   3  
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_8:8,Field_8:8,Field_8:8,Field_8:8?numbers=0",
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|    Field_8    |    Field_8    |    Field_8    |    Field_8    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),
           
("Field_32:32?numbers=0",
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_16:16,Field_16:16?numbers=0",
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Field_16           |            Field_16           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),
           
("Field_16:16,Field_8:8,Field_8:8?numbers=0",
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Field_16           |    Field_8    |    Field_8    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),           

("Field_32:32,Field_32:32?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),
           
("Field_32:32,Field_16:16?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Field_16           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_32:32,Field_24:24?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Field_24                   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_32:32,Field_31:31?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                           Field_31                          |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_32:32,Field_33:33?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_33                           |
+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| |
+-+"""),

("Field_32:32,Field_39:39?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_39                           |
+             +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|             |
+-+-+-+-+-+-+-+"""),

("Field_32:32,Field_56:56?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_56                           |
+                                               +-+-+-+-+-+-+-+-+
|                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_32:32,Field_16:16,Field_33:33?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Field_16           |                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|             Field_33            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_32:32,Field_16:16,Field_56:56?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Field_16           |                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                               +
|                            Field_56                           |
+               +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|               |
+-+-+-+-+-+-+-+-+"""),

("Field_32:32,Field_16:16,Field_32:32?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            Field_32                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Field_16           |            Field_32           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_8:8,Field_8:8,Field_8:8,Field_8:8,Field_12:12,Field_17:17,Field_22:22,Field_8:8,Field_5:5?numbers=0", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|    Field_8    |    Field_8    |    Field_8    |    Field_8    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|        Field_12       |             Field_17            |     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|               Field_22              |    Field_8    | Field_5 |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_16:16,Field_8:8,Field_8:8?numbers=0,bits=16", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Field_16           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|    Field_8    |    Field_8    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_16:16,Field_32:32?numbers=0,bits=16", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Field_16           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                               |
+            Field_32           +
|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_64:64?numbers=0,bits=16", 
"""+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                               |
+                               +
|                               |
+            Field_64           +
|                               |
+                               +
|                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_64:64?bits=64", 
""" 0                   1                   2                   3                   4                   5                   6      
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                            Field_64                                                           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Source Port:16,Destination Port:16,Sequence Number:32,\
Acknowledgment Number:32,Offset:4,Res.:4,Flags:8,Window:16,Checksum:16,\
Urgent Pointer:16,Options:24,Padding:8",
""" 0                   1                   2                   3  
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Source Port          |        Destination Port       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                        Sequence Number                        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                     Acknowledgment Number                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Offset|  Res. |     Flags     |             Window            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Checksum           |         Urgent Pointer        |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options                    |    Padding    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"""),

("Field_32:32?numbers=0,startchar=1,endchar=2,oddchar=3,evenchar=4,sepchar=5", 
"""14343434343434343434343434343434343434343434343434343434343434342
5                            Field_32                           5
14343434343434343434343434343434343434343434343434343434343434342"""),

]


# List of invalid test cases. It contains incorrect protocol specs.
invalidcases=[
"Field_64:64?bits=",
"Field_64:64?bits=A",
"Field_64:64?bits=0",
"Field_64:64?bits=-1",
"Field_64:0",
"Field_64:-1",
"Field_8:8,Field_8:0",
"Field_32:32?numbers=X",
"Field_32:32?numbers=",
"Field_32:32?startchar",
"Field_32:32?startchar=",
"Field_32:32?startchar=AAA",
"Field_32:32?endchar",
"Field_32:32?endchar=",
"Field_32:32?endchar=AAA",
"Field_32:32?oddchar",
"Field_32:32?oddchar=",
"Field_32:32?oddchar=AAA",
"Field_32:32?evenchar",
"Field_32:32?evenchar=",
"Field_32:32?evenchar=AAA",
"Field_32:32?sepchar",
"Field_32:32?sepchar=",
"Field_32:32?sepchar=AAA",
"Field_32:32?unknown",
"Field_32:32?",
"Field_32:32FieldThatContains?Sign",
"Field_32:32?sepchar=A,",
"Field_32:32,Field_8?sepchar=A,",
"Field_32:32,Field_8:?sepchar=A,",
"Field_32:32,Field_8:12,?sepchar=A,"
]


class ProtocolTests(unittest.TestCase):

    def test_regular_specs(self):
        """
        This function tests correctness for a number of known specs. It 
        instances a Protocol() passing a particular expect and then it compares
        the str() of the instance with the expected ASCII protocol header.
        """
        for i in range(0, len(validcases)):
            print("Testing Valid Spec '%s'" % validcases[i][0])
            p = protocol.Protocol(validcases[i][0])
            self.assertEqual(str(p), validcases[i][1])

    def test_invalid_specs(self):
        """
        This function tests the Protocol class for input validation. A number of
        invalid specs are passed. The constructor of the class is expected to raise
        the appropriate exceptions.
        """
        for i in range(0, len(invalidcases)):
            print("Testing Invalid Spec '%s'" % invalidcases[i])
            self.assertRaises(protocol.ProtocolException, protocol.Protocol, invalidcases[i])

if __name__ == '__main__':
    # Print our fancy ASCII header
    print("#########################################################################")
    print("#             ____            _                  _                      #")
    print("#            |  _ \ _ __ ___ | |_ ___   ___ ___ | |                     #")
    print("#            | |_) | '__/ _ \| __/ _ \ / __/ _ \| |                     #")
    print("#            |  __/| | | (_) | || (_) | (_| (_) | |                     #")
    print("#            |_|   |_|  \___/ \__\___/ \___\___/|_|                     #")
    print("#                                                                       #")
    print('#                 == "Protocol" Test Suite ==                           #')
    print("#                                                                       #")
    print("#########################################################################")
    # Run the actual tests
    unittest.main()
    

