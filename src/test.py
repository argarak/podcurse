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

# Import all needed libraries
import urwid
import feedparser
import mutagen
from mpd import MPDClient

# Initialise MPD
client = MPDClient()
client.timeout = None
client.idletimeout = None
client.connect("localhost", 6600)

# Start test RSS feed
feed = feedparser.parse('http://feeds.feedburner.com/WelcomeToNightVale')

palette = [
    ('artist', '', '', '', '#ffa', '#60d'),
    ('podcast', '', '', '', 'g50', '#60a'),
    ('title', '', '', '', 'g38', '#808')
]

def input_handle(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

def button_click(button, i):
    id = client.addid(feed.entries[i].enclosures[0].href, 0)
    client.playid(id)
    

# Header    
header_text = "1: Playlist | 2: Podcasts | 3: Search gPodder.net | 4: Add RSS | 5: Options"

header_column = [
    urwid.Text(u"Author"),
    urwid.Text(u"Podcast"),
    urwid.Text(u"Time"),
    urwid.Text(u"Episode")
]

header_w = [
    urwid.Text(header_text, align="center"),
    urwid.Divider(u'―'),
    urwid.Columns(header_column),
    urwid.Divider(u'―')
]

header = urwid.BoxAdapter(urwid.ListBox(urwid.SimpleListWalker(header_w)), 4)
# end Header

# Body
body = []

element = {'length': '0:00'}

for i in range(0, len(feed.entries)):
    body.append(urwid.Columns([
        urwid.Padding(urwid.Text(("artist", u"" + feed.entries[i].author)), ('relative', 50), 'pack'),
        urwid.Text(u"" + feed.feed.title),
        urwid.Text(u"0:00"),
        urwid.Padding(urwid.Button(u"" + feed.entries[i].title, on_press=button_click, user_data=i), align='left', width=('relative', 50)),
    ]))
# end Body
    
# Footer
footer_w = [
    urwid.Divider(u"="),
]

print(client.currentsong())
if hasattr(client.currentsong(), 'title') == True:
    footer_w.append(urwid.Columns([
        urwid.Text(client.currentsong()['title']),
        urwid.Text(u"[0:00/0:00]")
    ]))
else:    
    footer_w.append(urwid.Columns([
       urwid.Text(client.currentsong()['file']),
       urwid.Text(u"[0:00/0:00]")
    ]))
    
footer = urwid.BoxAdapter(urwid.ListBox(urwid.SimpleListWalker(footer_w)), 2)
# end Footer

listbox_body = urwid.ListBox(urwid.SimpleListWalker(body))

frame = urwid.Frame(
    urwid.ListBox(urwid.SimpleListWalker(body)),
    header,
    footer,
)
loop = urwid.MainLoop(frame, palette, unhandled_input=input_handle).run()
