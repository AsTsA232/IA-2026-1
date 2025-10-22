from leds import leds
lp=leds()

class controlador:
    def __init__(self):
        print("Controlador inicializado")

# Clasificación de las entradas en valores 'descritos'
    def hum_suelo(self, sensor_humedad):
        if sensor_humedad < 0.3:
            return 'Muy humedo'
        elif 0.3 <= sensor_humedad <= 0.7:
            return 'Humedo'
        elif 0.7 < sensor_humedad <= 1:
            return 'Seco'

    def luz_ambiental(self, luxometro):
        if luxometro < 0.02:
            return 'Poca'
        elif 0.02 <= luxometro <= 0.166:
            return 'Moderada'
        elif 0.166 < luxometro <= 1:
            return 'Mucha'

    def reglas_bomba(self, humedad_suelo):
        if humedad_suelo == 'Seco':
            return 1  
        else:
            return 0  
    
    def reglas_lampara(self, humedad_suelo, luz_amb):
        if humedad_suelo == 'Seco' and luz_amb == 'Mucha':
            return 'No encendido'
        elif humedad_suelo == 'Seco' and luz_amb == 'Moderada':
            return 'Enciende la mitad'
        elif humedad_suelo == 'Seco' and luz_amb == 'Poca':
            return 'Enciende la mitad'
            
        elif humedad_suelo == 'Humedo' and luz_amb == 'Mucha':
            return 'No encendido'
        elif humedad_suelo == 'Humedo' and luz_amb == 'Moderada':
            return 'Enciende la mitad'
        elif humedad_suelo == 'Humedo' and luz_amb == 'Poca':
            return 'Enciende todo'

        elif humedad_suelo == 'Muy humedo' and luz_amb == 'Mucha':
            return 'No encendido'
        elif humedad_suelo == 'Muy humedo' and luz_amb == 'Moderada':
            return 'No encendido'
        elif humedad_suelo == 'Muy humedo' and luz_amb == 'Poca':
            return 'Enciende la mitad'


    def compute_lux(self, luxometro, sensor_humedad):
        fuzz_lux = self.luz_ambiental(luxometro)
        fuzz_hum = self.hum_suelo(sensor_humedad)
        act = self.reglas_lampara(fuzz_hum, fuzz_lux)
        return act

    def compute_hum(self, sensor_humedad):
        fuzz_hum = self.hum_suelo(sensor_humedad)   
        act = self.reglas_bomba(fuzz_hum)
        return act
    
    def compute_lam(self, lampara):
        if lampara=='No encendido':
            lp.off()
        elif lampara=='Enciende la mitad':
            lp.media_luz()
        elif lampara=='Enciende todo':
            lp.luz_completa();