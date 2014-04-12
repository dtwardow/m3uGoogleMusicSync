import sys
from musicsync import MusicSync

if len(sys.argv) == 2:
    ms = MusicSync("twardowsky@gmail.com","zgbeknufxctrjvxn")
    # I use two-factor auth, so the password in my case is a generated "one-time" password
    ms.sync_playlist(sys.argv[1])
else:
    print "usage: %s <filename>" % sys.argv[0]

