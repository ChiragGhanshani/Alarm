#!/usr/bin/env python

import time
from subprocess import call

def timer():
	hours = raw_input('Please input the number of hours you would like the alarm to wait before ringing ')
	minutes = raw_input('Please input the number of minutes you would like the alarm to wait before ringing ')
	seconds = raw_input('Please input the number of seconds you would like the alarm to waid before ringing ')
	option = raw_input('Please input \'p\' if you would like to use a playlist for the alarm or \'m\' if you would like to use a song ')
	hours = int(hours)
	minutes = int(minutes)
	seconds = int(seconds)
	timer = (hours * 3200) + (minutes * 60) + seconds
	if option == 'p' or option == 'P':
		music = raw_input('please input the name of the playlist text file you would like to use ')
		time.sleep(timer)
		call('mplayer -loop 0 -shuffle -playlist ' + music, shell=True)		
	else:
		music = raw_input('Please input the name of the music file you would like to play when the alarm rings ')
		time.sleep(timer)
		call("mplayer -loop 0 " + music, shell=True)

timer()
