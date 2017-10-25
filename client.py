import gps
import time
import pubnub#pubnub==4.0.2
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import json

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-e2aa1c80-b6f9-11e7-b8f2-c6027b8a2e05"
pnconfig.publish_key = "pub-c-b3b3434d-7fbb-4ce6-bcc2-6762382de1d4"

pubnub = PubNub(pnconfig)

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

def show(msg, stat):
    if msg and stat: print( msg.timetoken, stat.status_code )
    else           : print( "Error", stat and stat.status_code )

while True:
	report = session.next()
	gps_dict=[]
	
	if report['class'] == 'TPV':
	    if hasattr(report, 'lat'):
		lat = report.lat
		gps_dict.append(report.lat)
	if report['class'] == 'TPV':
	    if hasattr(report, 'lon'):
		lng = report.lon
		gps_dict.append(report.lon)
		
	if bool(gps_dict):
		time.sleep(2)
		final = json.dumps(gps_dict) 
		pubnub.publish().channel("logging").message(gps_dict).async(show)
		print gps_dict
