import requests
import json

def taurus(serial):
    global _serial
    _serial = serial

def write_dActuator(actID, value):
    url = 'http://update.taurussystem.com/ws/webresources/Digital/set?key=%s&actuator=%s&value=%s' % (_serial, actID, value)
    r=requests.get(url)
    #print r.status_code
    #print r.headers
    #print r.content

def read_dActuator(actID):
    url = 'http://update.taurussystem.com/ws/webresources/Digital/get?key=%s&&actuator=%s' % (_serial, actID)
    r=requests.get(url)
    #print r.status_code
    #print r.headers
    #print r.content
    response = json.loads(r.content)
    return response["valor"]

def write_aActuator(actID, value):
    url = 'http://update.taurussystem.com/ws/webresources/Analog/set?key=%s&actuator=%s&value=%s' % (_serial, actID, value)
    r=requests.get(url)
    #print r.status_code
    #print r.headers
    #print r.content

def read_aActuator(actID):
    url = 'http://update.taurussystem.com/ws/webresources/Analog/get?key=%s&&actuator=%s' % (_serial, actID)
    r=requests.get(url)
    #print r.status_code
    #print r.headers
    #print r.content
    response = json.loads(r.content)
    return response["valor"]    

def write_sensor(sensorID, value):
    url = 'http://update.taurussystem.com/ws/webresources/Sensor/set?key=%s&sensor=%s&value=%s' % (_serial, sensorID, value)
    r=requests.get(url)
    #print r.status_code
    #print r.headers
    #print r.content

def read_sensor(sensorID):
    url = 'http://update.taurussystem.com/ws/webresources/Sensor/get?key=%s&&sensor=%s' % (_serial, sensorID)
    r=requests.get(url)
    #print r.status_code
    #print r.headers
    #print r.content
    response = json.loads(r.content)
    return response["valor"]      
