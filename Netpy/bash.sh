#!/bin/bash
USERNAME=someUser
#HOSTS="host1 host2 host3"
HOSTS="192.168.1.232"
SCRIPT="pwd; ls"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done
