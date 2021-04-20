import json, time

from boltiot import Bolt

myBolt = Bolt(<API key>,<Device ID>)

def readSensor():

      print("Reading LDR sensor value")

     input = myBolt.analogRead("A0")

     data=json.loads(input)

     print("LDR sensor value is " + str(data["value"]))

     return data

 

def buzzeron():

     output = myBolt.digitalWrite("0", "HIGH")

     return output

 

def buzzeroff():

     output = myBolt.digitalWrite("0", "LOW")

     return output

 

data1 = read()

value1 = int(data1["value"])

while True:

     time.sleep(5)

     data2 = read()

     value2 = int(data2["value"])

     value1 = value1 + 500

     if value2>value1:

         buzzeron()

         time.sleep(5)

         buzzeroff()

     value1 = value2