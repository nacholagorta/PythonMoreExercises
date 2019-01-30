
class Corcho(object):
    nombreBodega = "Vinos del sur"

    def __init__(self,nombreBodega):
        self.nombreBodega = nombreBodega

    def getNombre(self):
        return  self.nombreBodega


class Botella(Corcho):
    def __init__(self,corcho):
        self.corcho = corcho

class Sacacorchos(Botella):
    nombre = "Heineken"

    def __init__(self,corcho,botella):
        self.corcho = corcho
        self.botella = botella


    def getNombre(self):
        return  self.corcho
    def getBotella(self):
        return self.botella

    def abrirBotella(self,corcho,botella):
        print("El corcho de "+ corcho.getNombre()+" ha sido destapado")

    def sacarCorcho(self,corcho):
        print("El corcho " + corcho.getNombre() +" se tira a la basura")


corcho = Corcho("CORCHO")
botella = Botella(corcho)
sacacorchos = Sacacorchos(corcho,botella)

sacacorchos.abrirBotella(corcho,botella)
sacacorchos.sacarCorcho(corcho)