import dht
import machine

d = dht.DHT22(machine.Pin(23))
d.measure()
print (d.temperature())
print (d.humidity())


