#!/usr/bin/env python
# Detect Python that is not version 2 and try to use python2
import sys
import subprocess as sp
import inspect
from os import path

if sys.version_info.major != 2:
    python_2_path = str(sp.check_output('which python2', shell=True))
    python_2_path = python_2_path[2:-3]
    this_script = path.abspath(inspect.getfile(inspect.currentframe()))
    try:
        sp.call([python_2_path, this_script])
    except OSError:
        print('Unable to find Python 2. This script requires Python 2 to run')
        sys.exit(1)

    sys.exit(0)

import dbus
import gobject
import time
import tweepy

from dbus.mainloop.glib import DBusGMainLoop

consumer_key ='uGfo2bQjcYKpVRbrv60A'
consumer_secret ='ch8VE1UE6T7Sse0msibAnyyhF84mBWRBnC4ov3wTM'

access_token = '32486690-hL9lfQpmbguUMBnQeNN7QfexHMWFYOUAaFp3FQUI1'
access_token_secret = 'eIMJMqrF8sornQHxuir4rqT7oi7tkvpjULdHfHtDGkI'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

def handler(sender, dict, arr):
    try:
        if dict['Metadata']:
            api = tweepy.API(auth)
            message = '%s - %s #nowplaying http://bit.ly/YfR1Nm' % (', '.join(dict['Metadata']['xesam:artist']), dict['Metadata']['xesam:title'])

            api.update_status(message)

            # Do not resume waiting for a whole minute
            time.sleep(60)
    except tweepy.TweepError as e:
        print('%s %s' % (time.strftime('[%x %X]'), e))
    except KeyError:
        pass

DBusGMainLoop(set_as_default=True)

session_bus = dbus.SessionBus()
session_bus.add_signal_receiver(handler,
                                dbus_interface='org.freedesktop.DBus.Properties',
                                signal_name='PropertiesChanged',
                                path='/org/mpris/MediaPlayer2')

loop = gobject.MainLoop()
loop.run()
