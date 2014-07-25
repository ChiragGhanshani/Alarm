import time
from subprocess import call

hours = raw_input('Please input the number of hours you would like the alarm to wait before ringing')
minutes = raw_input('please input the number of minutes you would like the alarm to wait before ringing')
music = raw_input('please input the name of the music file you would like to play when the alarm rings')

hours = int(hours)
minutes = int(minutes)
seconds = (hours * 3200) + (minutes * 60)

time.sleep(seconds)

call("mplayer -loop 0 " + music, shell=True)
