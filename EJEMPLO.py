class Persona:
    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
        print ('Nombre:', self.nombre)


persona1=Persona()
persona1.inicializar('Eddy')
persona1.imprimir()

persona2=Persona()
persona2.inicializar('Karla')
persona2.imprimir()


persona3=Persona()
persona3.inicializar('Víctor')
persona3.imprimir()