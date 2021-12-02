
class Calculadora:

    def __init__(self, numero_1, numero_2):
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def somar(self):
        return self.numero_1 + self.numero_2
    def mostrar_soma(self):
        print("{} mais {} é {}".format(self.numero_1,self.numero_2,self.somar()))

    def subtrair(self):
        return self.numero_1 - self.numero_2

    def mostrar_sub(self):
        print("{} menos {} é {}".format(self.numero_1,self.numero_2,self.subtrair()))

    def multiplicar(self):
        return self.numero_1 * self.numero_2

    def mostrar_multi(self):
        print("{} multiplicado por {} é {}".format(self.numero_1,self.numero_2,self.multiplicar()))

    def dividir(self):
        return self.numero_1 / self.numero_2

    def mostrar_divi(self):
        print("{} dividido por {} é {}".format(self.numero_1,self.numero_2,self.dividir()))

    def exponenciar(self):
       return self.numero_1 ** self.numero_2

    def mostrar_expon(self):
        print("{} elevado a {} é {}".format(self.numero_1,self.numero_2,self.exponenciar()))
