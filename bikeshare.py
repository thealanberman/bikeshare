#!/usr/bin/env python

"""Foobar.py: Description of what foobar does."""

__author__      = "Barack Obama"
__copyright__   = "Copyright 2009, Planet Earth"

import requests, smtplib

def main():
    stationId = 65
    url = "http://feeds.bayareabikeshare.com/stations/stations.json"
    r = requests.get(url)
    stations = r.json()['stationBeanList']
    response = ""

    for item in stations:
        if item['id'] == stationId:
            if item['availableBikes'] < 2 or item['availableDocks'] < 2:
                response = str(item['availableBikes']) + " bikes left. "
                response += str(item['availableDocks']) + " open docks. "
                response += "%s (#%s)" % (item['stationName'], item['id'])
    return { 'response': response }

main()

def getStationStatus(station, stationId):
