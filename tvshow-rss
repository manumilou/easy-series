#!/bin/bash

DOWNLOAD_DIR=`grep dir_library /home/pi/.podget/podgetrc | cut -d "=" -f 2`
MEDIACENTER=zbox
TRANSMISSION_WATCH=/storage/downloads/watch

LIST=`grep -r karmorra /home/pi/.podget/serverlist  | cut -d ' ' -f 3`

# Download new torrent files
podget
# Copy torrent files to mediacenter if up
ping -c 1 -w 5 $MEDIACENTER &>/dev/null

if [ $? -ne 0 ] ; then
   echo "$MEDIACENTER is down!" 
else
   echo "$MEDIACENTER is up!" 
   scp $DOWNLOAD_DIR/tvshows/all/*.torrent $MEDIACENTER:$TRANSMISSION_WATCH
   rm -rf $DOWNLOAD_DIR/tvshows/all/*.torrent
fi

exit 0
