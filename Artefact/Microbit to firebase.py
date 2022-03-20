#import libraries
from firebase import firebase
import serial

#Connect tofirebase database
myDB = firebase.FirebaseApplication('https://rain-sensor-468f7-default-rtdb.firebaseio.com/', None)

#Serial Setup
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"
ser.open()

count = 0
while count < 10:
    #read in and edit data
    microbitdata = str(ser.readline())
    rain = microbitdata[2:]
    rain = rain.replace(" ", "")
    rain = rain.replace("b", "")
    rain = rain.replace("\\r\\n", "")
    rain = rain.replace("'", "")
    rain = int(rain)
      
    #write data to firebase
    upload = {
        "Rain" : rain
    }    
    myDB.post('/rainSensor/', upload)


ser.close()
    