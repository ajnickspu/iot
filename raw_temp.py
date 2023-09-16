import esp32

temp = esp32.raw_temperature()
tc = (temp-32.0)/1.8

print (tc)


