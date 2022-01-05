#!/usr/bin/env python3
import subprocess, math, re, time, atexit
from blinkt import set_pixel, set_brightness, show, clear

#GLOBALS#
bufferList = []

class Network:
    def tokenize_Cmd(self):
        for line in subprocess.run([self], capture_output=True, text=True).stdout.splitlines():
            bufferList.append(line)
        return [sub.split() for sub in bufferList]

    def get_Quality(self):
        rawData=self[5][1].split("=")
        splitData=re.split("/", str(rawData[1]))
        quotient = int(splitData[0]) / int(splitData[1])
        conv_quotient = quotient / 12.5
        return math.floor(conv_quotient * 100)
    
    def tokenize_ESSID(self):
            return [sub.split() for sub in self[0]]
    
    def get_ESSID(self):
        l_replace = [s.replace('ESSID:"', '') for s in self[3]]
        self[3] = l_replace
        lastItem = len(self) - 1
        li_replace = [s.replace('"', '') for s in self[lastItem]]
        self[lastItem]  = li_replace
        ESSID = ""
        x = 3
        while x <= lastItem:
            ESSID = ESSID +" ".join(map(str, self[x]))+ " "
            x += 1
        return ESSID


iwconfig = Network.tokenize_Cmd("iwconfig")
bufferList.clear()
#print (Network.get_Quality(iwconfig))
tokenized_essid = Network.tokenize_ESSID(iwconfig)
print (Network.get_ESSID(tokenized_essid))