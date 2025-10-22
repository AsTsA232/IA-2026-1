from machine import Pin, SoftI2C, PWM, ADC
class leds:
    def __init__(self):
        print("")
    
    def off(self):
        #3 leds
        led_r1=PWM(Pin(16))
        led_r1.freq(1000)
        led_a1=PWM(Pin(17))
        led_a1.freq(1000)

        #2 leds
        led_r2=PWM(Pin(18))
        led_r2.freq(1000)
        led_a2=PWM(Pin(19))
        led_a2.freq(1000)
        
        led_r1.duty_u16(65535) 
        led_a1.duty_u16(65535)
        led_r2.duty_u16(65535) 
        led_a2.duty_u16(65535)
        return 'Leds apagados'
            
    def media_luz(self):
                #3 leds
        led_r1=PWM(Pin(16))
        led_r1.freq(1000)
        led_a1=PWM(Pin(17))
        led_a1.freq(1000)

        #2 leds
        led_r2=PWM(Pin(18))
        led_r2.freq(1000)
        led_a2=PWM(Pin(19))
        led_a2.freq(1000)
        
        led_r1.duty_u16(65535) 
        led_a1.duty_u16(65535)
        led_r2.duty_u16(20000) 
        led_a2.duty_u16(5535)
        return 'Luz media'
            
    def luz_completa(self):
                #3 leds
        led_r1=PWM(Pin(16))
        led_r1.freq(1000)
        led_a1=PWM(Pin(17))
        led_a1.freq(1000)

        #2 leds
        led_r2=PWM(Pin(18))
        led_r2.freq(1000)
        led_a2=PWM(Pin(19))
        led_a2.freq(1000)
        
        led_r1.duty_u16(20000) 
        led_a1.duty_u16(5535)
        led_r2.duty_u16(20000) 
        led_a2.duty_u16(5535)
        return 'luz completa'
