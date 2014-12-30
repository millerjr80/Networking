#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nullroute.py
#  
#  Copyright 2014 Jonathan Miller <jonathan@routingloops.co.uk>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

# Import time, will be used to determine the description
import time
# Import socket to validate the IP's entered
import socket

# Specify the variables 
today = time.strftime("%Y%m%d")
conf = str("conf\n!")
add_fam = str("router static address-family ipv4 unicast\n!")
commit = str("commit\n!")

# Function to check if the IP is valid
def is_valid_ipv4_address(ip):
    try:
        socket.inet_pton(socket.AF_INET, ip)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(ip)
        except socket.error:
            return False
        return ip.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

# Request IP's be input, seperated by spaces
ip = raw_input("Insert IP's seperated by a space: ")

# Split the IP's and put them into a list
all_ips = map(str,ip.split())
print(" ")
print("----------------------------------------------------\n----------------------------------------------------")
print("To enter Configuration mode use:\n")
print(conf)
print(add_fam)
print(" ")
print("----------------------------------------------------\n----------------------------------------------------")
print("Copy and paste the output bellow into the router:")
print(" ")

# Repeat null route command for each IP entered
for x in all_ips:
	if is_valid_ipv4_address(x)==True:
		print x+"/32 null0 description "+today+"\n!"
		
	else:
		print(x+" Is not a valid IP address format")

print("----------------------------------------------------\n----------------------------------------------------")

print(" ")
print("To remove the null routes use the following:")
print(" ")

# Repeat "no" null route command for each IP entered
for y in all_ips:
	if is_valid_ipv4_address(y)==True:
		print "no "+y+"/32 null0\n!"
		
	else:
		print(y+" Is not a valid IP address format")

print("----------------------------------------------------\n----------------------------------------------------")
