
class CifradoSuper:

    p1="ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuwxyz0123456789";
    p2="1Zz2Yy3Xx0Tt4Ww5Uu6Oo7Pp8rR9SsNnMmKkLlHhIiJjEeFfDdCcBbAa1Zz2Yy3Xx0Tt4Ww5Uu6Oo7Pp8rR9SsNnMmKkLlHhIiJjEeFfDdCcBbAa";
    cadena=""

    def __init__(self, cadena):
        self.cadena = cadena
        # print("2:",self.cadena)


class CifrarCadena(CifradoSuper):
    pass

    def CifrarCaracter(self):
        c=""
        cc=""
        x=0
        cadenacifrada=""
        # print("texto3:",self.cadena)
        # print("tipo3:",type(self.cadena))
        tamano = len(self.cadena)
        # print("tamano:",tamano)
        for i in range(x, tamano):
            # print(i)
            c=self.cadena[i]
            cc=self.caractercifrado(c, tamano, i)
            cadenacifrada += cc
            # print("cadena posicion:",c)
            # print("cc:",cc)
            # print("cadena-cifrada:",cadenacifrada)


        return cadenacifrada



    def caractercifrado(self, c, tamano_cadena, i):
        cc=""
        indice=0
        if self.p1.index(c) != -1:
            indice=self.p1.index(c)+tamano_cadena+i
            # print("indice",indice)
            cc=self.p2[indice]


        return cc




# if __name__ == '__main__':
#     # d = CifradoSuper('CADE')
#     d1 = CifrarCadena('CADE')
#     print("1:",d1.CifrarCaracter())
    





