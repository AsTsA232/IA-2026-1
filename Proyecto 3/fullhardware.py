from machine import Pin, SoftI2C, PWM, ADC
from bh1750 import BH1750
import time
from controlador import controlador

c = controlador()

i2c = SoftI2C(scl=Pin(1), sda=Pin(0), freq=400000)
l = BH1750(bus=i2c, addr=0x23)

sm_sensor=ADC(Pin(26))
relay=Pin(20,Pin.OUT)


try:
    while True:
        lux = l.luminance(BH1750.CONT_HIRES_1)
        lux_nm=c.luz_ambiental(lux/3000)
        hum_nm=sm_sensor.read_u16()/66000
        hum=c.hum_suelo(hum_nm)
        luz=lux/3000
#impresion de medidas--------------------------------------    
        print("Luminosidad: {:.2f} lux".format(luz))
        print(lux_nm)
        print("Humedad: {:.2f} ".format(hum_nm))
        print(hum)
#salida a bomba-------------------------------------------
        relay.value(c.compute_hum(hum_nm))
#salida lampara-------------------------------------------
        lampara=c.compute_lux(luz,hum_nm)
        c.compute_lam(lampara)
        
        time.sleep(5)
        
except Exception as e:
    print("An error occurred:", e)