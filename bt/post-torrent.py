#
# Script to be executed by transmission when torrent is done downloading.
# Moves the finished file to a proper directory so that XBMC could scan it.
#

import os
import shutil
import logging
import json

# debug
# os.environ['TR_TORRENT_NAME'] = "New.Girl.S03E14.720p.HDTV.X264-DIMENSION [PublicHD]"
# os.environ['TR_TORRENT_DIR'] = "/storage/downloads"

# Init logging system
logging.basicConfig(filename='/storage/downloads/posttorrent.log',level=logging.DEBUG)
logging.info(os.environ['TR_TORRENT_NAME'])
logging.info(os.environ['TR_TORRENT_DIR'])

tr_torrent_name=os.environ['TR_TORRENT_NAME']
src_dir="/storage/downloads"

def move_file(file, src, dest):
    src_file = os.path.join(src, file)
    dest_file = os.path.join(dest, file)
    shutil.move(src_file, dest_file)
    logging.info("File " + os.environ['TR_TORRENT_NAME'] + " moved to " + dest)

# print src_dir, dest_dir, tr_torrent_name

json_data=open('/storage/settings.json')
data=json.load(json_data)
for i,j in data.iteritems():
    patterns = j["patterns"].split()
    for pattern in patterns:
        if tr_torrent_name.find(pattern) != -1:
            dest_dir = j['dir']
            # We have a match
            move_file(tr_torrent_name, src_dir, j['dir'])
            break;

json_data.close()
move_file(tr_torrent_name, src_dir, "/storage/cinema")
