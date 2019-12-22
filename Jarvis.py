import os
import sys

os.system('rm dump.dat')
os.system('lsblk | grep sd | cut -f1-2 -d" "> dump.dat')

with open('dump.dat','r') as f:
    for data in f:
        # convert data to list->l
        l = list(data)

        #remove non-ascii chars from list l [1-3]
        l[1:3]=""

        #echo to screen. now remove what we don't need.
        print(l[4:8])

        #now convert to standard string.
        dev = l[4:8]

        device=""

        for char in dev:
            device+= char
        print(device)

        #plug string to terminal commands ( create dir's to mount)
        os.system('cd .. && cd .. && cd .. && cd /media && mkdir'+ device)

        #ount each device to each dir.
        os.system('mount /dev/'+device+' /media/'+device)





