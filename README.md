# podcurse

## Summary

*Podcurse* will be a command line program to aggregate and play podcasts using the (Music Player Daemon)[http://www.musicpd.org/]. Its graphical user interface will be similar to (ncmpcpp)[https://github.com/arybczak/ncmpcpp]'s.

*Podcurse* will use the (urwid)[https://github.com/wardi/urwid] python library, which is based on (ncurses)[https://www.gnu.org/software/ncurses/], for the GUI.

Some functionalities that will be added to *podcurse* are:
	* Ability to play podcasts added to your playlist
	* Save playlists and have them continue from where you left off
	* Search gPodder.net to find podcasts
	* Add custom RSS
	* View and add subscribed podcasts to your playlist

Currently, *podcurse* is under development and not yet usable.

## Installing

To test *podcurse* you will need these libraries:
	* urwid
	* feedparser
	* python-mpd2

To install all these libraries (on a *nix system with python installed) at once type:

`pip install urwid feedparser python-mpd2`

Or:

`easy_install urwid feedparser python-mpd2`

## Contributing

At this point in time, I will not accept pull requests as this project is very young. As I release a stable, working version I will accept new features/bug fixes.

## License

See [COPYING][]. Copyright (c) 2015 Jakub Kukiełka.

[COPYING]: ./COPYING
