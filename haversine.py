import math
import numpy as py

R = 6371
aLat = math.radians(-6.1227369)
aLong = math.radians(106.6388715)
bLat = math.radians(-6.11006)
bLong = math.radians(106.6733806)

dLong = bLat - aLat
dLat = bLong - aLong

a = math.pow(math.sin(dLat/2), 2) + math.cos(aLat) * math.cos(bLat) * math.pow(math.sin(dLong/2), 2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d = R * c
jarak = round(d * 1000) / 1000

print(jarak)