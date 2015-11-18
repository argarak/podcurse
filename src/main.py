#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of podcurse.

# Podcurse is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Podcurse is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with podcurse.  If not, see <http://www.gnu.org/licenses/>.

# Import needed files
from libraries import *
import playlist
import podcasts
import search
import rss
import options

# Initialise MPD
client = MPDClient()
client.timeout = None
client.idletimeout = None
client.connect("localhost", 6600)

panels = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False
}

palette = [
    ('1: Playlist', 'white', 'light red'),
]

def input_handle(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    if key in '1' and panels[1] == True:
        playlist_init()
    if key in '2' and panels[2] == True:
        podcasts_init()
    if key in '3' and panels[3] == True:
        search_init()
    if key in '4' and panels[4] == True:
        rss_init()
    if key in '5' and panels[5] == True:
        options_init()

def button_click(button, i):
    id = client.addid(feed.entries[i].enclosures[0].href, 0)
    client.playid(id)
    

# Header    
header_text = "1: Playlist | 2: Podcasts | 3: Search | 4: Add RSS | 5: Options".split(' | ')

header_top = []

for i in header_text:
    header_top.append(urwid.Text((i, i)))
    
map1 = urwid.AttrMap(header_top[0], 'streak')
fill1 = urwid.Filler(map1)    
    
header_column = [
    urwid.Text(u"Author"),
    urwid.Text(u"Podcast"),
    urwid.Text(u"Time"),
    urwid.Text(u"Episode")
]

header_w = [
    urwid.GridFlow(header_top, 20, 5, 0, 'center'),
    urwid.Divider(u'―'),
    urwid.Columns(header_column),
    urwid.Divider(u'―')
]

map2 = urwid.AttrMap(header_w[0], 'streak')
fill2 = urwid.Filler(map2)    

header = urwid.BoxAdapter(urwid.ListBox(urwid.SimpleListWalker(header_w)), 4)
# end Header

# Body
body = []

element = {'length': '0:00'}
    
# Footer
footer_w = [
    urwid.Divider(u"="),
]

print(client.currentsong())

if True == True:
    footer_w.append(urwid.GridFlow([
        urwid.Text(u"None"),
        urwid.Text(u"[0:00/0:00]")
    ], 20, 50, 0, 'center'))

footer = urwid.BoxAdapter(urwid.ListBox(urwid.SimpleListWalker(footer_w)), 2)
# end Footer

listbox_body = urwid.ListBox(urwid.SimpleListWalker(body))

frame = urwid.Frame(
    urwid.ListBox(urwid.SimpleListWalker(body)),
    header,
    footer,
)
loop = urwid.MainLoop(frame, palette, unhandled_input=input_handle).run()
