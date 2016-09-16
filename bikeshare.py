#!/usr/bin/env python

"""bikeshare.py: Sends alerts as bikes or docks become scarce at key times."""

__author__ = "Alan Berman"

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
