class Persona:
    def inicializar(self,nom,sueldo):
        self.nombre=nom
        sefl.sueldo=suel

    def imprimir(self):
        print 'Nombre:'
        print self.nombre
        print '<br>'
        print 'Sueldo: '
        if self.sueldo>500:
        	print 'El empleado paga impuestos'

persona1=Persona()
persona1.inicializar('Eddy')
persona1.imprimir(' 1000')
#persona1.imprimir()
