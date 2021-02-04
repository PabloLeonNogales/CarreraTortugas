# APLICACIÓN CARRERA DE TORTUGAS

import turtle
import random

class Circuito():
    __nparticipantes = 0
    __colores = ('green', 'purple', 'red', 'blue', 'orange', 'violet', 'yellow', 'brown', 'black', 'white')
    
    def __init__ (self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.participantes = []
        self.__screen = turtle.Screen()
        self.__screen.setup(self.ancho, self.alto)
        self.__screen.bgcolor('lightgray')
        self.__screen.title("CARRERA DE TORTUGAS")
        self.__salida = -self.ancho/2+20
        self.__llegada = self.ancho/2-40
        
    def participan(self, *nombre):
        if nombre == None:
            print('Participan: {}'.format(self.participantes))
        else:
            self.__nparticipantes = len(nombre)
            
            for i in range (self.__nparticipantes):
                newTurtle = turtle.Turtle()
                newTurtle.color(self.__colores[i])
                newTurtle.shape('turtle')
                newTurtle.penup()
                newTurtle.setpos(self.__salida, (20*(1-self.__nparticipantes)+40*i))
                self.participantes.append([nombre[i],newTurtle])
            
    def competir(self):
        sigue = True
        while sigue:
            for i in range (self.__nparticipantes):
                self.participantes[i][1].fd(random.randint(5,10))
                if self.participantes[i][1].pos()[0] >= self.__llegada:
                    self.__screen.title("¡¡¡BRAVO!!! ¡¡¡Ha ganado {}!!!".format(self.participantes[i][0]))
                    self.participantes[i][1].write(self.participantes[i][0].upper(),False, "right", ("arial", 14, "bold italic"))
                    sigue = False
                    break
        
if __name__ == '__main__':
    c = Circuito(600,400)
    c.participan('Juan','Mayte', 'José', 'Carlos','Andrés')
    c.competir()