#!/bin/bash

rm /opt/bot/scripts/speedtest.png

speedtest-cli --secure --share > /opt/bot/scripts/speedtest.log

RESULTLINK=$(cat /opt/bot/scripts/speedtest.log | grep -o "\<http://[a-z0-9./-]*\>")

wget -P /opt/bot/scripts $RESULTLINK -O /opt/bot/scripts/speedtest.png > /dev/null 2>&1
