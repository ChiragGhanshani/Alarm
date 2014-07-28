Requirements:
	Python 2.7.3
	MPlayer (sudo apt-get install mplayer <- Debian)

To install this script, simply add it to your path and call it from the terminal.

To select the music file for the alarm, ensure that it is in the directory form which you are calling
alarm.py.

To use the playlist feature, the name of a text file containing all of absolute paths for the songs
you would like to play must be be given to the program when it asks for the playlist. One easy way to
make make this file is to use 'find'.
	Example: if all of the music files you want in your playlist are in your ~/Music/ directory and
		all of them are mp3 files, you can type the following into your command line to quickly
		generate a playlist:
			'find /home/<yourHomeDirectory>/Music/ -iname '*.mp3' > playlist.txt
		playlist.txt can then be given to alarm.py when it asks for the name of the playlist file.

Planned Features:
	Exact time specification for the alarm (eg. 8AM) <complete>
	Play playlists of music (possibly based on the day of the week) <complete>
	auto snooze <in progress>
	{more features will be added as I think of them}
