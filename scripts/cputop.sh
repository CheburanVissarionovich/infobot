#!/bin/bash
echo '```'
top -b -n 1 -o %CPU | sed '1,23!d'
echo '```'
