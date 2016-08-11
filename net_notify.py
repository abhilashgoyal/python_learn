#Readme: please install 'sudo apt-get install gnustep-gui-runtime' before running this script to make your system speak.  
#Readme: run this script as 'python net_notify_2.py yourname'  example 'python net_notify_2.py narendra'
'''
    File name: net_notify.py
    Author: Abhilash Goyal
    Date created: 03/08/2016
    Date last modified: 10/08/2016
    Python Version: 2.7
'''
import os
import time
import sys

def internet_on():
    if os.system("ping -c 1 8.8.8.8 > /dev/null 2>&1") == 0:	
	return 1
    else: 
	return 0

def test_network(dis="User"):
    try:
    	flag_online = 0
    	flag_offline = 0  
    	lastsave = 0  
    	while(True):
			flag = internet_on()
			time.sleep(0.5)
			if ((time.time() - lastsave > 300) and flag == 0 ):
				os.system('notify-send "'+dis+'" "'+"Sorry!! Still Ofline"+'"')
				lastsave = time.time()
			
			if (flag == 1 and flag_online==0):
				flag_offline = 0
				flag_online = 1
				lastsave = 0
				os.system('notify-send "'+dis+'" "'+"Congratulations !!! You are Online"+'"')
				os.system('say Online  > /dev/null 2>&1')
				
			if(flag == 0 and flag_offline==0):
				flag_online = 0
				flag_offline = 1
				os.system('notify-send "'+dis+'" "'+"Sorry!! Still Ofline"+'"')
				os.system('say Offline  > /dev/null 2>&1')
    except KeyboardInterrupt:
        print '\nInterrupted:   Bye'
        exit(0)

username= ''
try:
	user_name = str(sys.argv[1])
except:
	user_name = raw_input('Enter your name: ') #name you want to display in prompt

test_network(user_name)
	
	
	
