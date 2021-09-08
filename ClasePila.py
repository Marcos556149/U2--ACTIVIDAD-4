import numpy as np
class Pila:
    __items=None
    __tope1=0
    __tope2=0
    __cant=0
    def __init__(self,xcant):
        self.__items= np.empty(xcant,dtype=int)
        self.__tope1= -1
        self.__tope2=xcant
        self.__cant=xcant
    def vacia(self,numPila):
        if numPila == 1:
            return self.__tope1 == -1
        elif numPila == 2:
            return self.__tope2 == self.__cant
        else:
            print("Numero de pila incorrecto")
    def insertar(self,numPila,x):
        if numPila == 1:
            if self.__tope1 < (self.__tope2 - 1):
                self.__tope1 += 1
                self.__items[self.__tope1] = x
                return x
            else:
                print("Pila 1 llena")
                return 0
        elif numPila == 2:
            if self.__tope2 > (self.__tope1 + 1):
                self.__tope2 -= 1
                self.__items[self.__tope2]=x
                return x
            else:
                print("Pila 2 llena")
                return 0
        else:
            print("Numero de pila incorrecto")
    def suprimir(self,numPila):
        if self.vacia(numPila):
            print("Pila {} Vacia".format(numPila))
        else:
            if numPila == 1:
                x= self.__items[self.__tope1]
                self.__tope1 -= 1
                return x
            elif numPila == 2:
                x=self.__items[self.__tope2]
                self.__tope2 += 1
                return x
            else:
                print("dentro del su")
                print("Numero de pila incorrecto")
    def mostrar(self,numPila):
        if self.vacia(numPila):
            print("Pila {} Vacia".format(numPila))
        else:
            if numPila == 1:
                for i in range(self.__tope1,-1,-1):
                    print(self.__items[i])
            elif numPila == 2:
                for i in range(self.__tope2,self.__cant,+1):
                    print(self.__items[i])
            else:
                print("Numero de pila incorrecto")
