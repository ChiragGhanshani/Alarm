#!/usr/bin/env python

import time
from subprocess import call
from multiprocessing import Process

control = True

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
		Snooze = Process(target=snooze)
		Snooze.start()
		Snooze.join()
		call('mplayer -slave -input file=mplayerControl -loop 0 -shuffle -playlist ' + music, shell=True)	
	else:
		music = raw_input('Please input the name of the music file you would like to play when the alarm rings ')
		time.sleep(timer)
		Snooze = Process(target=snooze)
		Snooze.start()
		Snooze.join()
		call("mplayer -slave -input file=mplayerControl -loop 0 " + music, shell=True)

def alarm():
	hour = int(raw_input('Please enter the hour of day at which you would like to wake up in 24-hour HH format'))
	minute = int(raw_input('Please enter the minute of the hour at which you would like to wake up in the MM format'))
	option = raw_input('Please input \'p\' if you would like to use a playlist for the alarm or \'m\' if you would like to use a song ')
	x = 0
	if option == 'p' or option == 'P':
		music = raw_input('please input the name of the playlist text file you would like to use ')
	else:
		music = raw_input('Please enter the name of the music file you would like to play')
	while x == 0:
		awaken = time.localtime()
		if awaken.tm_hour == hour and awaken.tm_min == minute:
			x = x + 1
	if option == 'p' or option == 'P':
		Snooze = Process(target=snooze)
		Snooze.start()
		Snooze.join()
		call('mplayer -slave -input file=mplayerControl -loop 0 -shuffle -playlist ' + music, shell=True)
	else:
		Snooze = Process(target=snooze)
		Snooze.start()
		Snooze.join()
		call('mplayer -slave -input file=mplayerControl -loop 0 ' + music, shell=True)

def snooze():
	while control:
		time.sleep(60)
		call("echo p > mplayerControl", shell=True)
		time.sleep(300)
		call("echo p > mplayerControl", shell=True)
	call('echo q > mplayerControl', shell=True)

choice = int(raw_input('Please enter 1 to use the alarm function or 2 to use the timer'))
if choice == 2:
	Timer = Process(target=timer)
	Timer.start()
	Timer.join()
	time.sleep(100)
	end = raw_input()
	if end == 'q' or end == 'Q':
		control = False
else:
	Alarm = Process(target=alarm)
	Alarm.start()
	alarm.join()
	time.sleep(100)
	end = raw_input()
	if end == 'q' or end == 'Q':
		control = False
