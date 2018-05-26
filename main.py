#!/usr/bin/env python
#coding:UTF-8

##### NOTE ######
# data format
# field[0] = ID
# field[1] = dateadded
# field[2] = URL
# field[3] = URL status
# field[4] = threat
# field[5] = tags
# field[6] = urlhaus_link
#################

## set constant
# Database Server URL
URL = 'https://urlhaus.abuse.ch/downloads/csv/'

## download file path and filename
download_path = './'
download_filename = 'urlhaus_malicious_list.txt'

## import module
import urllib2

## set variable

## main code
response = urllib2.urlopen(URL)

file = open(download_path + download_filename,'w')

for line in response:
    if line.find('#') == 0 or line.find('offline') > -1:
        continue
    field = [x.strip('"') for x in line.split(',')]
    if field[4] == "":
        continue
    file.write(field[4] + ',' + field[2] + ',' + field[1] + '\n')

file.close()