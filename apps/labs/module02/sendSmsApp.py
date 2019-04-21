'''
Created on 13-Apr-2019

@author: Adhira
'''
import sys,os

sys.path.insert(0,'/home/pi/workspace/iot-device/connected-devices-python/apps')

from time import sleep
from labs.module02 import sendSMSTemp

# Initialize the object of TempSensorEmulator.
# sysPerfAdaptor = sendSMS.sendSMS()
sysPerfAdaptor = sendSMSTemp.sendSMSTemp()

sysPerfAdaptor.daemon = True
print("Starting system performance app daemon thread...")


# Call the start method as to call the run method in TemSensorEmulator thread class.
sysPerfAdaptor.start()
while (True):
    sleep(10)